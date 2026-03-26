# Importamos la libreria de flask
from flask import Flask
# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

# Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
@app.route("/")
def hello():
    return "hola Manuel"

# Y así se vería una aplicación con Python-flask

# Correr la aplicación, en la terminal debemos primero entrar en la carpeta:
# python .\app\hello.py
# Luego podemos arrancar la app con el comando: flask --app app.hello run
# Si nuestro archivo no estaría dentro de la carpeta app el comando sería:
# flask --app hello run