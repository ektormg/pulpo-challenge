# Pulpo Technical Challenge

## Intro

Este proyecto es elaborado por Héctor Moreno García para la empresa Pulpo, como parte de su technical challenge. El reto consiste en implementar una cola de mensajes utilizando Redis y desarrollar una API para poder manipular la cola.

## Instalación

Las instrucciones para reproducir el challenge están consideradas para Linux (Debian based) como sistema operativo, y la existencia de las siguientes condiciones:

**Requisitos:**
* Linux
* Python3
* El paquete ```git``` para poder clonar el repositorio
* Los paquetes ```pip```, ```virtualenv```

**Instalación de Redis:**

Primero hay que actualizar los paquetes:
```bash
sudo apt update
```
Después instalar el paquete ```redis-server```
```bash
sudo apt install redis-server
```
Para comprobar que el servidor Redis está funcionando correctamente se puede ejecutar el siguiente comando:
```bash
redis-cli PING
```
Si el resultado es *PONG*, está funcionando correctamente.
![ping](https://user-images.githubusercontent.com/64225038/202320579-a2949abc-df56-48c9-839a-337969963308.png)
Si apareciera error, se debe ejecutar el siguiente comando: ```redis-server```

**Descarga del repositorio y creación del ambiente virtual:**

Una vez instalado Redis, se puede descargar el repositorio con el siguiente comando:
```bash
git clone https://github.com/ektormg/pulpo-challenge.git
```
![git-clone](https://user-images.githubusercontent.com/64225038/202321106-8a9b6722-6944-4e3e-82ed-22590f928079.png)

El ambiente virtual se puede crear ejecutando el siguiente comando:
```bash
virtualenv venv
```
![venv](https://user-images.githubusercontent.com/64225038/202321558-d2311dc9-514f-48ea-927d-6f07f699276b.png)


Una vez creado el ambiente virtual, se activa, después hay que cambiar al directorio pulpo-challenge, y se instalan los requerimientos incluidos en el archivo ```requirements.txt```
```bash
source venv/bin/activate
cd pulpo-challenge
pip install -r requirements.txt
```
![pip-install](https://user-images.githubusercontent.com/64225038/202322352-4076af75-fa60-4241-b8cc-5ea882bd7d7c.png)


Ahora solo queda ejecutar Flask e ir al browser para acceder a la aplicación
```bash
export FLASK_DEBUG=1
export FLASK_APP=project
flask run
```
![flask-run](https://user-images.githubusercontent.com/64225038/202322764-1c32ffa3-b9b5-475a-8725-08d998228af7.png)


**Opcional**

Para procesar los mensajes de la cola se puede ejecutar, en el mismo directorio pulpo-challenge, el siguiente comando:
```bash
rq worker
```
![rq-worker](https://user-images.githubusercontent.com/64225038/202323058-03d1a846-4370-48e3-9edb-cb2f197e8ba0.png)


## Funcionamiento

Para acceder a la aplicación hay que ir a la siguiente dirección en el browser: http://127.0.0.1:5000

La aplicación cuenta con cuatro endpoints:  **Push** y **Pop** para manipular la cola, **Count** para obtener información sobre su número de mensajes, y **Health** para obtener información acerca del servidor Redis.
![index](https://user-images.githubusercontent.com/64225038/202304068-65e5c9c5-18bd-4bfe-a3f2-c5607d099d6a.png)
Adicionalmente, fue agregada la funcionalidad de inicio de sesión; para acceder a los endpoints, el usuario tendrá que registrarse en la aplicación o iniciar sesión con las siguientes credenciales: ```pulpo:pulpo```


**Registro de usuario / Inicio de sesión**

Para registrar un nuevo usuario dar click en **Registrarse**, ubicado en el menú de la parte superior derecha.
![registro](https://user-images.githubusercontent.com/64225038/202305822-3cf20cd3-5fb3-443b-a1b1-58fa302825b2.png)
Ingresar un nombre de usuario, crear una contraseña y dar click en **Crear usuario**.

Una vez dado de alta el nuevo usuario, se puede iniciar sesión con las credenciales recien creadas (o si no se desea crear un nuevo usuario pueden usarse las credenciales mencionadas arriba ```pulpo:pulpo```).

Después de iniciar sesión, se redireccionará nuevamente a la pantalla inicial, y se podrá observar el nombre de usuario en el menú superior de la derecha.
![logedin](https://user-images.githubusercontent.com/64225038/202308983-a5e4b808-df10-4575-899f-df04f40c7f1e.png)


**Push Endpoint**

En este endpoint se mandan los mensajes a la cola. Solo hay que escribir un mensaje y dar click en el botón **Agregar a la cola**.
![push](https://user-images.githubusercontent.com/64225038/202311544-c4fac59b-3390-4a9b-9cc5-f17f7478b193.png)
Después de agregar el mensaje, se recibe una notificación en donde se confirma el envío a la cola.


**Pop Endpoint**

En el Pop endpoint se puede eliminar un mensaje específico o todos los mensajes que se encuentren en ese momento en la cola.

Si desde el Push endpoint se crean y envían varios mensajes en la cola, éstos van a aparecer en la sección inferior de la pantalla **Lista de mensajes (IDs) en la cola**
![lista-pop](https://user-images.githubusercontent.com/64225038/202314576-588ed813-1924-4531-a1b7-2f08e2bc6ed3.png)
Para una fácil y rápida identificación, el ID del mensaje consta del mismo valor del mensaje y su timestamp correspondiente, con el fin de evitar IDs duplicados en caso de que se repitan los mensajes.

Para eliminar un mensaje en específico, se tiene que ingresar el ID del mensaje de la sección inferior. Se puede copiar y pegar el valor como se muestra en la imagen de abajo, y después dar click en el botón **Eliminar**.
![pop](https://user-images.githubusercontent.com/64225038/202315443-978c0c74-97aa-4a57-ab97-b04b050e5714.png)

Para borrar todos los mensajes en la cola se tiene que dar click en el botón **Borrar Todo**.


**Count Endpoint**

Aquí se puede ver el número de mensajes que actualmente existe en la cola, además se brinda la información equivalente al comando ```rq info```
![count](https://user-images.githubusercontent.com/64225038/202318568-f961b090-ee82-44b3-88dd-193294c65669.png)


**Health Endpoint**

En este endpoint adicional, se obtiene información acerca del estado de salud del servidor redis. Se realiza el chequeo al servidor con ```redis-cli PING``` y además se muestran las métricas del comando ```redis-cli info```
![health](https://user-images.githubusercontent.com/64225038/202319305-ae96b4c5-66eb-4df4-9966-114f826588e3.png)

## Docker

Otra alternativa que se tiene es utilizar Docker para ejecutar la aplicación. Los pasos que se describen a continuación consideran que ```docker``` se encuentra instalado y en funcionamiento.

Primero se descarga el repositorio desde Github.
```bash
git clone https://github.com/ektormg/pulpo-challenge.git
```
![docker-git](https://user-images.githubusercontent.com/64225038/202593755-4ac535a9-f54b-4b3a-8982-ab0e470d0ac9.png)

En el directorio pulpo-challenge se deberá crea el archivo **Dockerfile** con la siguiente información:
```bash
touch Dockerfile
nano Dockerfile
```
![touch-nano](https://user-images.githubusercontent.com/64225038/202600713-395d5492-dc5b-49cd-9938-aca9903b5088.png)
Contenido del archivo Dockerfile:
```bash
# syntax=docker/dockerfile:1

FROM ubuntu

RUN apt update

RUN apt install python3-pip -y

RUN apt install redis-server -y

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=project

CMD flask run -h 0.0.0.0 -p 5000
```
Con el siguiente comando se crea la imagen de la aplicación para Docker:
```bash
docker build -t pulpo-docker .
```
![image-success](https://user-images.githubusercontent.com/64225038/202603400-37831805-8c9c-4914-b061-8ce05dae05d6.png)
Una vez que se haya creado exitosamente la imagen, se puede verificar con el siguiente comando:
```bash
docker images
```
![docker-images](https://user-images.githubusercontent.com/64225038/202604084-bb6c0563-ec0a-4d34-ac78-6c15399d0f63.png)


Para ejecutar la aplicación se deberá ingresar el siguiente comando:
```bash
docker run -d -p 5000:5000 pulpo-docker
```
![docker-run](https://user-images.githubusercontent.com/64225038/202604359-d97cbfd2-8959-4d1e-b9d4-74b0efe1491d.png)

Por último, se deben iniciar el servidor Redis y el worker para procesar los mensajes de la cola. Antes, se debe ejecutar el siguiente comando para obtener el ID del Container que se acaba de inicializar.
```bash
docker ps
```
Una vez identificado el Container ID, ejecutar los siguientes dos comandos:
Para iniciar el servidor Redis
```bash
docker exec <ContainerID> redis-server
```
En una terminal distinta, ejecutar el worker:
```bash
docker exec <ContainerID> rq worker
```

Para acceder a la aplicación hay que ir a la siguiente dirección en el browser: http://127.0.0.1:5000
![app-docker](https://user-images.githubusercontent.com/64225038/202607859-21882217-00a1-4226-9d2f-69e5d8a6973e.png)



## Uso posible en cybersecurity

En tareas de cybersecurity, una cola de mensajes/tareas podría tener diversos usos. Dentro del Red Team se podría utilizar una cola de tareas en la etapa de reconocimiento de los pentests. Por ejemplo, se podría ejecutar la herramienta ```dirb``` para escanear directorios y subdirectorios en una dirección URL, pero con la cola de mensajes de Redis se podrían ingresar múltiples URLs y cada escaneo se iría a la cola de tareas para su procesamiento. Posteriormente se podrían revisar en un archivo .txt los resultados de los escaneos. Otro ejemplo podría ser su uso en el envío de emails en una campaña de phishing.

Para tareas del Blue Team, una cola de mensajes se podría implementar para levantar tickets que requieran atención del equipo de seguridad. El usuario podría ingresar en una aplicación su mensaje, nivel de prioridad, y tipo de problema (web app, servidores, accesos, etc.). El ticket iría a la cola de mensajes para su procesamiento y debida atención de parte del equipo de seguridad.


