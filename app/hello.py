# Importamos la libreria de flask
from flask import Flask
# importamos las rutas
from routes.rutas import rutas_bp

# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

app.register_blueprint(rutas_bp)

if __name__ == "__main__":
    app.run(debug=True)