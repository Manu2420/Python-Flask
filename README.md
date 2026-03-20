# Ptython - flask

<img src="./img/flask.png" alt="Logo flask" width="350" height="150">

Flask es un micro-framework web ligero y flexible para Python, diseñado para crear aplicaciones web, APIs y
microservicios de forma rápida y sencilla. Se basa en las herramientas **Werkzeug (WSGI)** y **Jinja (plantillas)**,
proporcionando solo las funcionalidades esenciales, lo que permite a los desarrolladores elegir sus propias
herramientas y bibliotecas adicionales.

flask cuenta con una gran comunidad y documentación en línea, es fácil encontrar soluciones a problemas comunes.

## Ventajas

- Fácil de utilizar
- Flexibilidad
- Pequeño y ligero
- Comunidad activa
- Bajo nivel de abstracción
- Fácil de intergrar con otros servicios

## Instalación

Para intalar flask tenemos 2 opciones:

- Global (en nuestro ordenador)
- Por proyecto (cada vez que necesitemos trabajar con flask)

Para trabajar con flask, necesitamos crear y/o instalar un entorno virtual.

El entorno virtual nos servira para gestionar las dependencias de nuestro proyecto. 

> ¿Qué problema resuelve un entorno virtual? Cuantos más proyectos de Python tengas, más probable es que necesites
> trabajar con diferentes versiones de librerías de Python, o incluso con el propio Python. Las nuevas versiones de las
> librerías para un proyecto pueden romper la compatibilidad en otro proyecto.
>
> flask documentation

Los entornos virtuales son grupos independientes de bibliotecas Python, uno para cada proyecto. Los paquetes instalados
para un proyecto no afectarán a otros proyectos o a los paquetes del sistema operativo.

Para crear el entorno virtual, utilizaremos los siguientes comandos en nuestra terminal o utilizando la terminal de 
**VS Code**.

```cmd
python -m venv nombre_entorno
```

Python viene con el módulo **_venv_** para crear entornos virtuales. [Python](https://docs.python.org/es/3.14/library/venv.html#creating-virtual-environments)

Entonces, el comando anterior quedaría así:

```cmd
python -m venv .venv
```

