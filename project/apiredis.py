from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from project.auth import login_required
from project.db import get_db
from datetime import datetime

import redis
from rq import Queue
from rq.job import Job
import time
import subprocess


# Make a connection of the queue and redis
r = redis.Redis()
q = Queue(connection=r)


bp = Blueprint('apiredis', __name__)

@bp.route('/')
def index():
    
    return render_template('apiredis/index.html')

#Function to just add tasks into the queue
def message():
	message= "Hellooo"
	time.sleep(100)
	return (message)

#Endpoint hello triggers function message
@bp.route("/api/queue/hello")
@login_required
def add_message():
	
	dt = datetime.now()
	dt_str = str(dt)
	job = q.enqueue(message, job_id=dt_str)
	
	return f"The task {job.id} is added into the task queue"
	
#This function is the concept of a task added into a queue, it is triggered by the Push Endpoint
def message3(message2):

	message_pushed = message2
	time.sleep(100)
	
	return message_pushed

#Endpoint Push uses a post method to add messages/tasks into the queue
@bp.route("/api/queue/push", methods=('GET', 'POST'))
@login_required
def push_msg():
	
	if request.method == 'POST':
		
		message2= request.form['msg1']
		dt = datetime.now()
		dt_str = str(message2)+" "+ str(dt)
		
		job2 = q.enqueue(message3, message2, job_id=dt_str)
		
		return render_template('apiredis/push.html', sent="Ok. Mensaje enviado a la cola: ", message2=message2)
		
	return render_template('apiredis/push.html')

#Endpoint Pop is used to delete a message/job from the queue
@bp.route("/api/queue/pop", methods=('GET', 'POST'))
@login_required
def pop_msg():

	if request.method == 'POST':
		message_pop = request.form['msg_pop']
	
		job = Job.fetch(message_pop, connection=r)
		job.cancel()
		
		
		return render_template('apiredis/pop.html',deleted="Ok. Mensaje eliminado: ", message_pop=message_pop, queued_job_ids = q.job_ids)
	
		
	return render_template('apiredis/pop.html',queued_job_ids = q.job_ids)

#Endpoint delete es usado para borrar todos los mensajes de la cola
@bp.route("/api/queue/delete", methods=('GET', 'POST'))
@login_required
def borrar_todo():
	
	q.empty()
	
	return redirect('/api/queue/pop')
	
#Endpoint count counts the number of tasks in the queue
@bp.route("/api/queue/count")
@login_required
def count_jobs():
	
		
	var2 = subprocess.Popen('rq info', shell=True, stdout=subprocess.PIPE).stdout.read()
	rqinfo_str= var2.decode()
	
	#return f"The number of messages in the queue is: {count}"
	return render_template('apiredis/count.html', count = len(q), rqinfo_str = rqinfo_str.split('\n'))
	
#Endpoint Health checa el estado de salud del servidor redis y provee otras estadísticas
@bp.route("/api/health", methods=('GET', 'POST'))
@login_required
def health():
	
	var = subprocess.Popen('redis-cli info', shell=True, stdout=subprocess.PIPE).stdout.read()
	redisinfo_str= var.decode()
	
	var3 = subprocess.Popen('redis-cli ping', shell=True, stdout=subprocess.PIPE).stdout.read()
		
	return render_template('apiredis/health.html', redisinfo_str = redisinfo_str.split('\n'), ping_str= var3.decode())
	
	
	
	
	
	
	
	
	
	
	
	
	
