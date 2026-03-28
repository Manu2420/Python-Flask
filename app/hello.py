# Importamos la libreria de flask
from flask import Flask
# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

# Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
@app.route('/')
def princ():
    return "hola Manuel"

# Y así se vería una aplicación con Python-flask

# Rutas
# ruta a la página index
@app.route('/index')
def index():
    return "Página principal"

# ruta a la pagina hello
@app.route('/hello')
def hello():
    return "Hola Manuel"

# Variables en ruta

@app.route('/nombre/<nombre>')
def nombre(nombre):
    return f"<h1>Hola {nombre}!</h1>"

# Varias rutas con variables
@app.route('/saludo')
@app.route('/saludo/<name>')
@app.route('/saludo/<name>/<int:age>')
def saludo(name = None, age = None):
    if name == None and age == None:
        return "<h1>Hola Mundo!</h1>"
    elif age == None:
        return f"<h1>Hola {name}!</h1>"
    else:
        return f"<h1>Hola {name}, tu edad es: {age} años y naciste en el año {2026 - age}.</h1>"

if __name__ == "__main__":
    app.run(debug=True)