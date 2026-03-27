# Importamos la libreria de flask
from flask import Flask
# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

# Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
#@app.route("/")
#def hello():
 #   return "hola Manuel"

# Y así se vería una aplicación con Python-flask

# Correr la aplicación, en la terminal debemos primero entrar en la carpeta:
# python .\app\hello.py
# Luego podemos arrancar la app con el comando: flask --app app.hello run
# Si nuestro archivo no esta dentro de la carpeta app el comando sería:
# flask --app hello run

# Podemos crear tantas rutas como necesitemos, por ejemplo: una ruta para registrarse, otra para el dashboard, otra para productos etc..
# Al crear una ruta, esta siempre debe contener una función.
# Por ejemplo, cambiaremos la ruta principal por un index y crearemos otra ruta para el hello.

# Ruta principal
@app.route("/")
def index():
    return f'<h1>Página principal</h1>'

# Ruta para hello
@app.route("/hello")
def hello():
    return f'<h1>Hola Manuel</h1>'

# Al correr la aplicación, nos mostrara la ruta principal con el texto Página principal.
# Ahora, si cambiamos la URL para que apunte a la ruta hello (http://127.0.0.1:5000/hello) nos mostrara el texto Hola Manuel.