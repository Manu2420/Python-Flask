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

"""
Rutas (@app.route())
"""

#Las rutas son el corazón de cualquier aplicación web con Flask. Si imaginas tu aplicación como un edificio, las rutas son las puertas que llevan a diferentes habitaciones.

#1. ¿Qué son y para qué sirven?
#Una ruta es la asociación entre una URL (lo que el usuario escribe en el navegador) y una función de Python (lo que quieres que suceda).

#Sirven para que el servidor sepa qué respuesta enviar según lo que el usuario pida.

    #Si el usuario pide /, le das la bienvenida.

    #Si pide /contacto, le muestras un formulario.

#2. ¿Cómo se crea una ruta?
#Se usa el decorador @app.route(). Justo debajo, debes definir una función que retorne algo (texto, HTML, JSON, etc.).

#@app.route('/saludo')
#def hola_mundo():
#    return "<h1>¡Hola desde Flask!</h1>"

#3. ¿Qué debe ir dentro de una ruta?
#Dentro de la función de la ruta (llamada view function), va toda la lógica de negocio. Normalmente verás estas tres etapas:

    #Recibir datos: Obtener información de la URL o de un formulario.

    #Procesar: Consultar una base de datos, hacer un cálculo o verificar una sesión.

    #Retornar: Enviar una respuesta al navegador (usualmente un render_template para mostrar una página HTML).

#4. ¿Cuántas rutas puedo tener?
#No hay un límite técnico. Puedes crear desde una sola ruta hasta miles.

    #En aplicaciones pequeñas, todas suelen ir en el mismo archivo.

    #En aplicaciones grandes, se usan Blueprints para organizar las rutas en archivos separados (por ejemplo: rutas_usuarios.py, rutas_productos.py).

#5. Rutas Dinámicas (Variables)
#No siempre querrás rutas fijas. A veces necesitas que la URL cambie según el dato, por ejemplo, el perfil de un usuario:

#@app.route('/usuario/<nombre>')
#def perfil(nombre):
#    return f"Hola, este es el perfil de {nombre}"

#Si entras a /usuario/manuel, la página dirá "Hola, este es el perfil de manuel".

#Tipos de métodos en las rutas
#Por defecto, las rutas solo aceptan peticiones GET (ver contenido). Si quieres que una ruta reciba datos de un formulario, debes especificar el método POST:

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        # Aquí procesas los datos del formulario
#        return "Iniciando sesión..."
#    return "Muestro el formulario de login"

#Resumen rápido
#Ruta: El camino (/inicio).

#Función: El guía que decide qué mostrar.

#Retorno: El destino final (lo que ve el usuario).

# Podemos crear tantas rutas como necesitemos, por ejemplo: una ruta para registrarse, otra para el dashboard, otra para productos etc..

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

"""
Activar el Debug 
"""

#Activar el modo Debug en Flask es fundamental porque nos permite dos cosas increíbles:
#Auto-Reload: El servidor se reinicia solo cada vez que guardamos un cambio en el código.
#Debugger Interactivo: Si hay un error, veremos una página en el navegador la cual nos permite ejecutar código para inspeccionar qué falló.

# Para activar el Debug, la forma más rápida y recomendable es la siguiente:

"""
Al final del código colocamos lo siguiente:

if "__name__ == __main__":
    app.run(debug=true)

¿Qué hace esto?

Ese bloque de código es una de las "piezas mágicas" más comunes en Python y sirve para controlar cómo se ejecuta tu archivo.

if __name__ == "__main__": Es el interruptor de seguridad.

Cuando ejecutas el archivo directamente: Python le asigna el nombre "__main__" a la variable interna __name__.
    Por lo tanto, la condición se cumple y el código de adentro se ejecuta.

Cuando importas el archivo desde otro lado: Si en otro archivo escribieras import app, Python no ejecutaría el servidor de Flask.
    Esto es vital para evitar que se abra una ventana o un servidor sin que tú lo quieras solo por querer usar una función de ese archivo en otro proyecto.

app.run(debug=True): Hace funcionar el servidor de flask, y el parámetro debug=true le da "superpoderes" mientras programamos.

Servidor Interactivo: Si cometes un error en el código, en lugar de que la página se quede en blanco o dé un error genérico, 
    Flask te mostrará en el navegador exactamente en qué línea falló y te permitirá probar comandos ahí mismo para entender el error.

Auto-recarga (Hot Reload): No tienes que detener y volver a ejecutar el servidor cada vez que guardas un cambio. 
    Flask detecta que guardaste el archivo y reinicia el servidor en menos de un segundo. Es extremadamente útil para trabajar rápido en Warp y ver los resultados al instante.

Acceso Local: Por defecto, esto abre el servidor en http://127.0.0.1:5000.

Si por algún motivo estamos trabajando con el puerto 5000 con otro proyecto, podemos cambiar el puerto de flask de la siguiente forma:

if "__name__ == __main__":
    app.run(debug=True, port=5001)

esto nos mostrara el servidor en http://127.0.0.1:5001.
""" 

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