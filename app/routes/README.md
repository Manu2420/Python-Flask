# Rutas @app.route()

Las rutas son el corazón de cualquier aplicación web con Flask. Si imaginas tu aplicación como un edificio, las rutas son las puertas que llevan a diferentes habitaciones.

## ¿Qué son y para qué sirven?

Una ruta es la asociación entre una `URL` (lo que el usuario escribe en el navegador) y una función de Python (lo que quieres que suceda).

Sirven para que el servidor sepa qué respuesta enviar según lo que el usuario pida.

- Si el usuario pide `/`, le das la bienvenida.

- Si pide `/contacto`, le muestras un formulario.

## ¿Cómo se crea una ruta?

Se usa el decorador `@app.route()`. Justo debajo, debes definir una función que retorne algo (`texto`, `HTML`, `JSON`, etc.).

```py
@app.route('/saludo')
def hola_mundo():

return "<h1>¡Hola desde Flask!</h1>"
```

## ¿Qué debe ir dentro de una ruta?

Dentro de la función de la ruta (llamada view function), va toda la lógica de negocio. Normalmente verás estas tres etapas:

- Recibir datos: Obtener información de la `URL` o de un formulario.
- Procesar: Consultar una base de datos, hacer un cálculo o verificar una sesión.
- Retornar: Enviar una respuesta al navegador (usualmente un `render_template` para mostrar una página `HTML`).

## ¿Cuántas rutas puedo tener?

No hay un límite técnico. Puedes crear desde una sola ruta hasta miles.

- En aplicaciones pequeñas, todas suelen ir en el mismo archivo.

- En aplicaciones grandes, se usan Blueprints para organizar las rutas en archivos separados (por ejemplo: `rutas_usuarios.py`, `rutas_productos.py`).

### Rutas Dinámicas (Variables)

No siempre querrás rutas fijas. A veces necesitas que la URL cambie según el dato, por ejemplo, el perfil de un usuario:

```py
@app.route('/usuario/<nombre>')
def perfil(nombre):
return f"Hola, este es el perfil de {nombre}"
```

Si entras a `/usuario/manuel`, la página dirá "Hola, este es el perfil de manuel".

### Tipos de métodos en las rutas

Por defecto, las rutas solo aceptan peticiones `GET` (ver contenido). Si quieres que una ruta reciba datos de un formulario, debes especificar el método `POST`:

```py
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí procesas los datos del formulario
        return "Iniciando sesión..."
    return "Muestro el formulario de login"
```

#### Resumen rápido

- Ruta: El camino (/inicio).
- Función: El guía que decide qué mostrar.
- Retorno: El destino final (lo que ve el usuario).

Podemos crear tantas rutas como necesitemos, por ejemplo: una ruta para registrarse, otra para el dashboard, otra para productos etc..

1. Ruta principal

```py
@app.route("/")
def index():
    return f'<h1>Página principal</h1>'
```

2. Ruta para hello

```py
@app.route("/hello")
def hello():
    return f'<h1>Hola Manuel</h1>'
```

Al correr la aplicación, nos mostrara la ruta principal con el texto Página principal.

Ahora, si cambiamos la URL para que apunte a la ruta hello (`http://127.0.0.1:5000/hello`) nos mostrara el texto Hola Manuel.

## Variables en rutas

Las variables en rutas de `Flask` son espacios dentro de la `URL` que capturan un valor y lo pasan como parámetro a tu función de vista (por ejemplo, un id, un nombre, un usuario, etc.).

En `Flask` las rutas normales son fijas, como:

```py
@app.route("/usuarios")
def listar_usuarios():
    return "Lista de usuarios"
```

Pero si quieres una ruta dinámica que cambie según el dato de la `URL`, defines una variable en la ruta así:

```py
@app.route("/usuarios/<nombre>")
def mostrar_usuario(nombre):
    return f"Hola, {nombre}!"
```

`/<nombre>` dice: “en esa parte de la URL voy a recibir un valor y se guardará en la variable nombre”.

Cuando el usuario entra a `http://localhost:5000/usuarios/Jeniffer`, `Flask` ejecuta `mostrar_usuario("Jeniffer")`.

### Sintaxis de la variable

La variable se escribe entre `<>` dentro de la ruta:

```py
@app.route("/articulos/<id>")
def mostrar_articulo(id):
    return f"Mostrando artículo con id {id}"
```

`id` es un parámetro de la función.

Si la ruta es `/articulos/3`, el valor 3 entra en `id`.

### Tipos de variables (convertidores)

Puedes forzar el tipo del valor:

```py
@app.route("/articulos/<int:id>")      # solo acepta enteros
@app.route("/precio/<float:valor>")    # solo acepta números con coma
@app.route("/ruta/<path:resto>")       # acepta partes con barras, como subdirectorios
```

Por defecto, sin tipo, `Flask` trata todo como `string`.

Resumen sencillo

Variable en ruta = parte de la `URL` que no es fija, se escribe como `<nombre>`.

Ese nombre debe coincidir con el nombre del parámetro de la función.

Sirve para construir `URLs` como `/usuarios/Jeniffer` o `/articulos/123` y procesar el valor en Python.

## Escape de HTML

El escape de HTML (o HTML Escaping) es una medida de seguridad crítica que consiste en convertir caracteres especiales de HTML en "entidades de texto" para que el navegador no los interprete como código, sino como simple texto.

Es tu principal defensa contra ataques de `XSS` (`Cross-Site Scripting`).

### ¿Por qué es necesario?

Imagina que tienes una ruta en `Flask` que recibe el nombre de un usuario y lo muestra en pantalla. Si un usuario malintencionado escribe esto en el campo de nombre:

```js
<script>alert('¡Hackeado!')</script>
```

Si no "escapas" ese texto, el navegador ejecutará el `script` y mostrará una alerta (o algo peor, como robar cookies). Al escapar el `HTML`, el navegador recibe esto:

```txt
&lt;script&gt;alert('¡Hackeado!')&lt;/script&gt;
```

Y lo que el usuario ve en pantalla es el texto literal del `script`, pero no se ejecuta.

### ¿Cómo lo maneja Flask?

La gran ventaja de `Flask` es que escapa el `HTML` por defecto cuando usas archivos de plantilla `.html` dentro de la carpeta templates.

- Ejemplo Seguro (Automático en `Jinja2`):
- Si en tu `hello.py` pasas una variable:
- return render_template('`index.html`', `usuario='<b>Manuel</b>'`)
- En el HTML (`index.html`):

```html
<p>Hola {{ usuario }}</p>
```

El navegador mostrará: `Hola <b>Manuel</b>` (con las etiquetas visibles), no pondrá la palabra Manuel en negrita.

### ¿Cuándo NO se escapa? (Uso del filtro | safe)

A veces, tú quieres que se renderice el `HTML` (por ejemplo, si traes texto formateado desde una base de datos de confianza). Para eso usas el filtro `safe`:

```html
#<p>Hola {{ usuario | safe }}</p>
```

### Escapar manualmente en Python

Si necesitas escapar un texto fuera de una plantilla (directamente en tu lógica de `Python`), `Flask` te ofrece la herramienta escape:

```py
from markupsafe import escape

@app.route("/<nombre>")
def hola(nombre):
    return f"Hola, {escape(nombre)}!"
```

Resumen: El escape de `HTML` convierte el código "vivo" en texto "muerto" para que tu aplicación sea segura y no permita que usuarios externos inyecten `scripts` maliciosos.
