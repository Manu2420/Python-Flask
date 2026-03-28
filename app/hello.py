# Importamos la libreria de flask
from flask import Flask
# instancia a flask (representa nuestra aplicación de flask)
app = Flask(__name__)

# Creamos una ruta, con el '/' le indicamos que esta será nuestra ruta principal
@app.route("/")
def hello():
    return "hola Manuel"

# Y así se vería una aplicación con Python-flask

"""
Escape de HTML
"""

#El escape de HTML (o HTML Escaping) es una medida de seguridad crítica que consiste en convertir caracteres especiales de HTML en "entidades de texto" para que el navegador no los interprete como código, sino como simple texto.

#Es tu principal defensa contra ataques de XSS (Cross-Site Scripting).

#1. ¿Por qué es necesario?
#Imagina que tienes una ruta en Flask que recibe el nombre de un usuario y lo muestra en pantalla. Si un usuario malintencionado escribe esto en el campo de nombre:

#<script>alert('¡Hackeado!')</script>

#Si no "escapas" ese texto, el navegador ejecutará el script y mostrará una alerta (o algo peor, como robar cookies). Al escapar el HTML, el navegador recibe esto:

#&lt;script&gt;alert('¡Hackeado!')&lt;/script&gt;
#Y lo que el usuario ve en pantalla es el texto literal del script, pero no se ejecuta.

#2. ¿Cómo lo maneja Flask?
#La gran ventaja de Flask es que escapa el HTML por defecto cuando usas archivos de plantilla .html dentro de la carpeta templates.

#Ejemplo Seguro (Automático en Jinja2):
#Si en tu hello.py pasas una variable:

#return render_template('index.html', usuario='<b>Manuel</b>')
#En el HTML (index.html):

#<p>Hola {{ usuario }}</p>
#El navegador mostrará: Hola <b>Manuel</b> (con las etiquetas visibles), no pondrá la palabra Manuel en negrita.

#3. ¿Cuándo NO se escapa? (Uso del filtro | safe)
#A veces, tú quieres que se renderice el HTML (por ejemplo, si traes texto formateado desde una base de datos de confianza). Para eso usas el filtro safe:

#<p>Hola {{ usuario | safe }}</p>

#4. Escapar manualmente en Python
#Si necesitas escapar un texto fuera de una plantilla (directamente en tu lógica de Python), Flask te ofrece la herramienta escape:

#from markupsafe import escape

#@app.route("/<nombre>")
#def hola(nombre):
#    return f"Hola, {escape(nombre)}!"

#Resumen: El escape de HTML convierte el código "vivo" en texto "muerto" para que tu aplicación sea segura y no permita que usuarios externos inyecten scripts maliciosos.

if __name__ == "__main__":
    app.run(debug=True)