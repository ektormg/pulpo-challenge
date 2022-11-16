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


## Funcionamiento
```bash
$ export FLASK_DEBUG=1
$ export FLASK_APP=project
$ flask run
```

## Mejoras



export FLASK_APP=project

export FLASK_DEBUG=1
