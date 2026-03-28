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