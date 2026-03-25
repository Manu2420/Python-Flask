# Ptython - flask

![Logo Flask](./img/flask.svg)

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

## Instalación Entorno Virtual

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

Para crear el entorno virtual, utilizaremos los siguientes comandos en nuestra terminal o utilizando la terminal de **VS Code**.

```cmd
python -m venv nombre_entorno
```

Python viene con el módulo **_venv_** para crear entornos virtuales. [Python](https://docs.python.org/es/3.14/library/venv.html#creating-virtual-environments),
también puedes visitar la página de [Flask](https://flask.palletsprojects.com/en/stable/installation/#virtual-environments) que también tiene una guía d instalación del entorno virtual.

Entonces, el comando anterior quedaría así:

```cmd
python -m venv .venv
```

Una vez ejecutado el comando, tenemos que activar el entorno virtual, para ello escribimos lo siguiente:

```cmd
.venv\Scripts\activate
```

Una vez ejecutado veremos que nuestra terminal coloca al principio y entre parentesis **(.venv)**.

Para ver los paquetes que se instalaron, utilizamos el siguiente comando:

```cmd
pip list
```

`pip list` mostrara un listado con los paquetes instalados al crear el entorno virtual **venv**.

Para desactivar el entorno virtual, basta con escribir en la terminal `deactivate`, esto detendra el entorno por completo.

### Archivo requirements.txt

El archivo `requirements.txt` en **Python** sirve para gestionar las dependencias de un proyecto, listando todas las
bibliotecas externas y sus versiones específicas necesarias para que el código funcione. Permite automatizar la
instalación de estos paquetes, garantizando que el entorno de desarrollo sea reproducible y consistente entre
diferentes equipos o servidores.

Para generar el archivo, podemos crearlo en la carpeta raíz de nuestro proyecto o utilizando el siguiente comando:

```cmd
pip freeze > requirements.txt
```

Este comando creara el archivo `requirements.txt`.

Este archivo nos facilita la instalación de todas las dependencias que estamos utilizando en nuestro proyecto y nos permite llevar un control ordenado de los paquetes necesarios.

Para ingresar las dependencias a nuestro archivo, tenemos dos opciones:

- Escribiendo manualmente el nombre de la dependencia en el archivo, por ejemplo "flask".
- La otra opción es, si ya instalamos las dependencias y no recordamos cuales son, ejecutamos el siguiente comando, el cual se encargara de escribirlos en el archivo por nosotros:
  
```cmd
pip install -r requirements.txt    
```

## Intalación de flask

Una vez creado el entorno virtual y requirements.txt, el siguiente paso es instalar el micro-framework flask en nuestro proyecto.

Para instalar flask desde la terminal, debemos utilizar el siguiente comando:

```cmd
pip install flask
```

Este comando instalara flask junto a otros paquetes que vienen con flask, como por ejemplo:

```code
Package      Version
------------ -------
blinker      1.9.0
click        8.3.1
colorama     0.4.6
Flask        3.1.3
itsdangerous 2.2.0
Jinja2       3.1.6
MarkupSafe   3.0.3
pip          25.1.1
Werkzeug     3.1.6
```

También podemos instalar otros paquetes como `bcrypt`, `PyMySQL`, `flask-mysqldb`, etc....

>[!IMPORTANT]
>Cada vez que tengamos que instalar un paquete, debemos detener el entorno virtual con `deactivate`, una vez instalado el paquete podemos volver a activar el entorno virtual.
