# Importamos Blueprint, render_template
from flask import Blueprint, render_template

rutas_bp = Blueprint('rutas', __name__)

# Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
#@rutas_bp.route('/')
#def princ():
#    return "hola Manuel"

# Si tenemos una plantilla podemos agregarla aquí utilizando render_template
@rutas_bp.route('/')
def princ():
    return render_template('index.html')


# ruta a la página index
@rutas_bp.route('/index')
def index():
    return "Página principal"

# ruta a la pagina hello
@rutas_bp.route('/hello')
def hello():
    return "Hola Manuel"

# Variables en ruta

@rutas_bp.route('/nombre/<nombre>')
def nombre(nombre):
    return f"<h1>Hola {nombre}!</h1>"

# Varias rutas con variables
@rutas_bp.route('/saludo')
@rutas_bp.route('/saludo/<name>')
@rutas_bp.route('/saludo/<name>/<int:age>')
def saludo(name = None, age = None):
    if name == None and age == None:
        return "<h1>Hola Mundo!</h1>"
    elif age == None:
        return f"<h1>Hola {name}!</h1>"
    else:
        return f"<h1>Hola {name}, tu edad es: {age} años y naciste en el año {2026 - age}.</h1>"
    
# Escape de HTML
#@rutas_bp.route('/code/<code>')
#def code(code):
#    if code == None:
#        return "<h1>Escape de HTML</h1>"
#    else:
#       return f'<code>{code}</code>'
#En principio esta ruta solo mostrara lo que le indiquemos en la url y en formato code de HTML.

# Si utilizamos path y enviamos un script de JS en la Url, este se ejecutara sin problema alguno, y es sumamente peligroso si no lo sabemos manejar.

#@rutas_bp.route('/code/<path:code>')
#def code(code):
#    if code == None:
#        return "<h1>Escape de HTML</h1>"
#    else:
#       return f'<code>{code}</code>' 

# Para que esto no ocurra, vamos a escapar el HTML importando la dependencia "markupsafe" que viene con flask.

from markupsafe import escape

@rutas_bp.route('/code/')
def code_default():
    return '<h1>Escape de HTML</h1>'

@rutas_bp.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>' 