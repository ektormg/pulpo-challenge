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

**Descarga del repositorio y creación del ambiente virtual:**

Una vez instalado Redis, se puede descargar el repositorio con el siguiente comando:
```bash
$ git clone https://github.com/ektormg/pulpo-challenge.git
```
El ambiente virtual se puede crear ejecutando el siguiente comando:
```bash
$ virtualenv venv
```
Una vez creado el ambiente virtual, cambiar al directorio pulpo-challenge e instalar los requerimientos incluidos en el archivo ```requirements.txt```
```bash
$ cd pulpo-challenge
$ pip -r install requirements.txt
```
Ahora ya solo queda ejecutar Flask e ir al browser para acceder a la aplicación
```bash
$ export FLASK_DEBUG=1
$ export FLASK_APP=project
$ flask run
```

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
Después de agregar el mensage, se recibe un mensaje en donde se confirma el env


## Mejoras



