# Importamos la libreria de flask
from flask import Flask
# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

#Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
@app.route("/")
def hello():
    return ("hola Manuel")

