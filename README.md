    Raúl Sánchez Fuentes Practica 2 IV
    Copyright (C) 2013  Raúl

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.




Raúl Sánchez Fuentes
==============================

### Práctica 2 de la asignatura Infraestructura Virtual de 2013

# DOCUMENTACIÓN

## LA PRÁCTICA

La práctica 2 de IV consiste en crear una mini-aplicación web (un hola mundo o un simple formulario) y aislarlo en una jaula chroot.

Para ello he escogido crear mi jaula con debootstrap, herramienta vista en clase con la cual instala un sistema basado en Debian dentro de un subdirectorio de otro sistema ya instalado. 

El sistema elegido para instalar es wheezy, también utilizado ya en clase, el cuál ha dado muy buen resultado, por ello he decidido instalar mi aplicación en este sistema.

La aplicación creada es un programa en python utilizando y web.py es un framework web para Python de uso sencillo pero suficientemente potente que permite desarrollar una aplicación web en poco tiempo.

Esta aplicación almacenara en un fichero las sugerencias para la asignatura IV, y también mostrará estas al realizar una.


## EL PROCESO

El primer paso es instalar la máquina mediante debootstrap. Vemos en esta captura la orden para ello:

![IV](https://dl.dropboxusercontent.com/s/ytv879qbbt4d6wn/p2.1.png)


El siguiente paso será entra en la jaula mediant chroot y comprobar que estamos dentro con un ls:

![IV](https://dl.dropboxusercontent.com/s/8qqb8kaf5wwv5i1/p2.2.png)


Una vez hecho esto vamos a proceder a instalar los paquetes que nos son necesarios:

* Python:

![IV](https://dl.dropboxusercontent.com/s/jofuwx5xtl12e8h/p2.3.png)


* Webpy:

![IV](https://dl.dropboxusercontent.com/s/a254pl1wyk532vf/p2.4.png)


Una vez tenemos todo instalado ya podemos pasar a crear nuestra aplicación. El código de esta esta disponible en los ficheros de la práctica.

Una vez creada la aplicación procedemos a lanzarla:

![IV](https://dl.dropboxusercontent.com/s/tdur1jdekiuxx8i/p2.10.png)

Rellenamos los datos que nos piden para la sugerencia:

![IV](https://dl.dropboxusercontent.com/s/rs5bfze2fkm8lxf/p2.6.png)

Y ya tenemos nuestra sugerencia almacenada, y podemos ver las sugerencias hasta el momento:

![IV](https://dl.dropboxusercontent.com/s/nj286oml7wdrmml/p2.7.png)


#CONCLUSIÓN

Una vez ya terminada la práctica se puede comprobar que se ha puesto en desarrollo lo aprendido en estas clases, mostrando la creación de la jaula, he instalando una aplicación en ella.
