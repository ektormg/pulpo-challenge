# Pulpo Technical Challenge

## Intro

Este proyecto es elaborado por Héctor Moreno García para la empresa Pulpo como parte de su technical challenge. El challenge consta de implementar una cola de mensajes utilizando Redis y desarrollar una API para poder manipular la cola.

## Instalación

Las instrucciones para reproducir el challenge están considerando el uso de Linux (Debian based) como sistema operativo, y la existencia de los siguientes requisitos:

**Requisitos:**
* Linux
* Python3
* El paquete ```git``` para poder clonar el repositorio
* Los paquetes ```pip```, ```virtualenv```

**Instalación de Redis:**

Primero actualizamos los paquetes:
```bash
$ sudo apt update
```
Después instalamos el paquete ```redis-server```
```bash
$ sudo apt install redis-server
```
Para comprobar que el servidor Redis está funcionando correctamente se puede ejecutar el siguiente comando:
```bash
$ redis-cli PING
```
Si el resultado es *PONG*, está funcionando correctamente.
![ping](https://user-images.githubusercontent.com/64225038/202320579-a2949abc-df56-48c9-839a-337969963308.png)


**Descarga del repositorio y creación del ambiente virtual:**

Una vez instalado Redis, se puede descargar el repositorio con el siguiente comando:
```bash
$ git clone https://github.com/ektormg/pulpo-challenge.git
```
![git-clone](https://user-images.githubusercontent.com/64225038/202321106-8a9b6722-6944-4e3e-82ed-22590f928079.png)

El ambiente virtual se puede crear ejecutando el siguiente comando:
```bash
$ virtualenv venv
```
![venv](https://user-images.githubusercontent.com/64225038/202321558-d2311dc9-514f-48ea-927d-6f07f699276b.png)


Una vez creado el ambiente virtual, lo activamos y después cambiamos al directorio pulpo-challenge e instalamos los requerimientos incluidos en el archivo ```requirements.txt```
```bash
$ source venv/bin/activate
$ cd pulpo-challenge
$ pip install -r requirements.txt
```
![pip-install](https://user-images.githubusercontent.com/64225038/202322352-4076af75-fa60-4241-b8cc-5ea882bd7d7c.png)


Ahora ya solo queda ejecutar Flask e ir al browser para acceder a la aplicación
```bash
$ export FLASK_DEBUG=1
$ export FLASK_APP=project
$ flask run
```
![flask-run](https://user-images.githubusercontent.com/64225038/202322764-1c32ffa3-b9b5-475a-8725-08d998228af7.png)


**Opcional**

Para procesar los mensajes de la cola se puede ejecutar, en el mismo directorio pulpo-challenge, el siguiente comando:
```bash
$ rq worker
```
![rq-worker](https://user-images.githubusercontent.com/64225038/202323058-03d1a846-4370-48e3-9edb-cb2f197e8ba0.png)


## Funcionamiento

Para acceder a la aplicación hay que ir en el browser a la siguiente dirección: http://127.0.0.1:5000

La aplicación cuenta con cuatro endpoints,  **Push** y **Pop** para manipular la cola, **Count** para obtener información del número de mensajes en la cola, y **Health** para obtener información a cerca del servidor Redis.
![index](https://user-images.githubusercontent.com/64225038/202304068-65e5c9c5-18bd-4bfe-a3f2-c5607d099d6a.png)
Adicionalmente, se agregó la funcionalidad de inicio de sesión y para acceder a los endpoints, el usuario tendrá que registrare en la aplicación o iniciar sesión con las siguientes credenciales: ```pulpo:pulpo```


**Registro de usuario / Inicio de sesión**

Para registrar un nuevo usuario se puede dar click en **Registrarse** ubicado en el menú de la parte superior derecha.
![registro](https://user-images.githubusercontent.com/64225038/202305822-3cf20cd3-5fb3-443b-a1b1-58fa302825b2.png)
Ingresar un nombre de usuario, crear una contraseña, y dar click en **Crear usuario**.

Una vez dado de alta el nuevo usuario, podrás iniciar sesión con las credenciales recien creadas (o si no quieres crear un nuevo usuario puedes usar las credenciales mencionadas arriba ```pulpo:pulpo```).

Después de iniciar sesión, serás redirigido de nuevo a la pantalla inicial, y podrás observar tu nombre de usuario en el menu superior de la derecha.
![logedin](https://user-images.githubusercontent.com/64225038/202308983-a5e4b808-df10-4575-899f-df04f40c7f1e.png)


**Push Endpoint**

En este endpoint se mandan los mensajes a la cola. Solo tienes que escribir un mensaje y dar click en el botón **Agregar a la cola**.
![push](https://user-images.githubusercontent.com/64225038/202311544-c4fac59b-3390-4a9b-9cc5-f17f7478b193.png)
Después de agregar el mensaje, se recibe un mensaje en donde se confirma el envío a la cola.


**Pop Endpoint**

En el Pop endpoint se puede eliminar un mensaje específico o todos los mensajes que se encuentren en ese momento en la cola.

Si desde el Push endpoint se crean y envían varios mensajes en la cola, éstos van a aparecer en la sección inferior de la pantalla **Lista de mensjaes (IDs) en la cola**
![lista-pop](https://user-images.githubusercontent.com/64225038/202314576-588ed813-1924-4531-a1b7-2f08e2bc6ed3.png)
Para una fácil y rápida identificación, el ID del mensaje consta del mismo valor del mensaje y su timestamp correspondiente con el fin de evitar IDs duplicados en caso que se repitan los mensajes.

Para eliminar un mensaje en específico, se tiene que ingresar el ID del mensaje de la sección inferior. Se puede copiar y pegar el valor como se muestra en la imagen de abajo, y después dar click en botón **Eliminar**.
![pop](https://user-images.githubusercontent.com/64225038/202315443-978c0c74-97aa-4a57-ab97-b04b050e5714.png)

Para borrar todos los mensajes en la cola se tiene que dar click en el botón **Borrar Todo**.


**Count Endpoint**

Aquí se puede ver el número de mensajes que actualmente existen en la cola, y además se brinda la información equivalente al comando ```rq info```
![count](https://user-images.githubusercontent.com/64225038/202318568-f961b090-ee82-44b3-88dd-193294c65669.png)


**Health Endpoint**

En este endpoint adicional, se obtiene información acerca del estado de salud del servidor redis. Se realiza el chequeo al servidor con ```redis-cli PING``` y además de muestran las métricas del comando ```redis-cli info```
![health](https://user-images.githubusercontent.com/64225038/202319305-ae96b4c5-66eb-4df4-9966-114f826588e3.png)



## Uso posible en cybersecurity




