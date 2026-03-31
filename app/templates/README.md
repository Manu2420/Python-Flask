# Plantillas

Las plantillas `Jinja2` + `HTML` son el “motor de vistas” de `Flask`: permiten escribir páginas `HTML` que se vuelven dinámicas, usando `variables`, `bucles`, `condicionales`, `herencia` y más, todo desde el mismo archivo `.html`.

## ¿Dónde se crean las plantillas?

`Flask` busca automáticamente las plantillas en una carpeta llamada `templates` al mismo nivel que tu archivo principal (`app.py`, `run.py`, etc.):

```text
mi_proyecto/
├── app.py
├── routes/
│   └── rutas.py
└── templates/          ← aquí van los HTML + Jinja2
    ├── base.html
    ├── index.html
    └── usuarios.html
```

Dentro de la carpeta `templates` creamos los archivos `.html` normales, pero con extensiones Jinja2 (`{{ ... }}`, `{% ... %}`).

## ¿Por qué se crean plantillas?

- Separar la lógica de `Python` de la presentación en `HTML`.

- Evitar repetir código `HTML` (por ejemplo, el menú o el pie de página).

- Generar `HTML` distinto según los datos que llegan de la base de datos o formularios.

Por ejemplo: creamos un `index.html` en la carpeta `templates`, para poder utilizarla como página principal, en el archivo `rutas.py` de la carpeta `routes` podemos llamarla utilizando `render_template` de la siguiente forma:

```py
@rutas_bp.route('/')
def princ():
    return render_template('index.html')
```

Ya que la ruta apunta a una página principal con `'/'`, nuestro `index.html` será nuestra página `html` principal.

## ¿Qué pueden contener?

Un archivo `templates/index.html` puede contener:

- `HTML` estándar.

- Variables de `Python`.

- Estructuras de control: `if`, `for`, `macros`, etc.

- Herencia de una plantilla `base.html`.

- Llamadas a funciones y filtros.

- `HTML` con enlaces a tus rutas y archivos estáticos (`css`, `js`).

Ahora veamos un ejemplo de cómo utilizar estructuras de control en `HTML`.

```py
@rutas_bp.route('/')
def inicio():
    # diccionario
    dato = {
        'titulo': 'Index',
        'bienvenida': '¡Saludos!'
    }
    return render_template('index.html', data=dato)
```

Bien, hemos creado un diccionario y lo pasamos al `render_template`. Ahora veamos el `HTML`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plantillas en Flask</title>
</head>
<body>
    <!-- Pasamos el diccionario al h1 -->
    <h1>{{ data }}</h1>
    
</body>
</html>
```

Salida:

```py
{'titulo': 'Index', 'bienvenida': '¡Saludos!'}
```

Ahora veamos cómo utilizar el diccionario en el `HTML`:

```html
<body>
    <!-- Pasamos el diccionario al h1 -->
    <h1>{{ data.bienvenida }}</h1>
    
</body>
```

Salida:

```text
¡Saludos!
```

Ahora vamos a cambiar el título de la página:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.titulo }}</title>
</head>
<body>
    <!-- Pasamos el diccionario al h1 -->
    <h1>{{ data.bienvenida }}</h1>
    
</body>
</html>
```

Salida:

![Salida](../../img/salida.png)

Ahora vamos a utilizar el bucle `for` en el `HTML`:

Vamos a crear una lista en la ruta para utilizarla con el bucle `for` para que nos muestre el contenido de la lista:

```py
@rutas_bp.route('/')
def inicio():
    # Lista
    cursos = ['PHP', 'Python', 'Java', 'JavaScript', 'MySQL', 'Kotlin']
    # vamos a utilizar un diccionario
    dato = {
        'titulo': 'Index',
        'bienvenida': '¡Saludos!'
        # agregamos la lista al diccionario
        'cursos': cursos,
        'num_cursos': len(cursos)
    }
    return render_template('index.html', data=dato)
```

Ahora vamos a utilizar la etiqueta `<ul>` para mostrar la lista con el bucle `for`:

```html
<body>
    <!-- Pasamos el diccionario al h1 -->
    <h1>{{ data.bienvenida }}</h1>
    
    <p>Cursos</p>
    <ul>
        <!-- Iniciamos el bucle for -->
        {% for c in data.cursos %}
        <li>{{ c }}</li>
        <!-- Terminamos el bucle for -->
        {% endfor %}
    </ul>
</body>
```

Salida:

![Salida](../../img/salida1.png)

Vamos a utilizar la condicional `if` para verificar que la lista sea mayor que 0, ósea, que tenga contenido, si no tiene contenido mostraremos un párrafo que diga "No hay cursos disponibles...":

```html
<body>
    <!-- Pasamos el diccionario al h1 -->
    <h1>{{ data.bienvenida }}</h1>
    
    <p>Cursos</p>
    <!-- Iniciamos la condicional if -->
    {% if data.num_cursos > 0 %}

    <ul>
        {% for c in data.cursos %}
        <li>{{ c }}</li>
        {% endfor %}
    </ul>
    <!-- Utilizamos la condicional else -->
    {% else%}
    <p>No hay cursos disponibles...</p>
    <!-- Terminamos la condicional if -->
    {% endif %}
</body>
```

Para que se vea mejor, vamos a colocar en 0 la variable `num_cursos`:

```py
dato = {
        'titulo': 'Index',
        'bienvenida': '¡Saludos!'
        # agregamos la lista al diccionario
        'cursos': cursos,
        'num_cursos': 0 # lo colocamos en 0
    }
```

Salida:

![Salida](../../img/salida2.png)

Y con la longitud de cursos:

![Salida](../../img/salida1.png)

## Herencia de Plantillas

La herencia en Jinja2 te permite definir una plantilla base con bloques reutilizables y luego extenderla en otras plantillas, evitando duplicar código y manteniendo un diseño consistente en tu aplicación Flask. Es una técnica clave para organizar tus vistas y mantener tu HTML modular y limpio.

### Concepto de Herencia en Jinja2

- Plantilla `base`: Define la estructura general (`doctype`, `<head>`, navegación, `footer`).
- Bloques (`block`): Son secciones que las plantillas hijas pueden sobrescribir.
- Extensión (`extends`): Permite que una plantilla hija herede de la base.

El nombre `bse.html` es solo una convención muy extendida en proyectos `Flask`/`Django` porque refleja claramente que esa plantilla es la “`base`” de la cual heredan las demás plantillas.

Pero técnicamente puedes llamarla como quieras: `layout.html`, `main.html`, `master.html`, etc.

Lo importante es:

- Que el archivo esté en la carpeta `templates/`.
- Que las plantillas hijas usen el mismo nombre en la directiva `{% extends "nombre.html" %}`.

>[!IMPORTANT]
>`base.html` es una convención, no una regla. Usarla ayuda a otros desarrolladores a entender rápido la estructura.

Veamos el esqueleto de `base.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página base - {% block title %}{% endblock %}</title>
</head>
<body>

    <h1>Página base de mi proyecto</h1>

    <p>A continuación se mostrará el contenido de la página Index, la cual extiende de esta página.</p>

    {% block content %}
    <!-- aquí irá el contenido de la página hija -->
    {% endblock %}
    
</body>
</html>
```

Plantilla `index.html`:

```html
<!-- vamos a extender este html de base.html -->

{% extends "base.html" %}

{% block title %} Index {% endblock %}

{% block content %}

<!-- desde aquí podemos volver a utilizar los bloques if y for -->

<!-- Pasamos el diccionario al h1 -->
<h1>{{ data.bienvenida }}</h1>

<p>Cursos</p>

<!-- Iniciamos la condicional if -->
{% if data.num_cursos > 0 %}
<ul>
    <!-- Iniciamos el bucle for -->
    {% for c in data.cursos %}
    <li>{{ c }}</li>
    <!-- Terminamos el bucle for -->
    {% endfor %}
</ul>
<!-- Utilizamos la condicional else -->
{% else%}
<p>No hay cursos disponibles...</p>
<!-- Terminamos la condicional if -->
{% endif %}

{% endblock %}
```

Como podemos observar, `index.html` no contiene la estructura base para crear una página `HTML` (`<!DOCTYPE html>`, `<html lang="es">`, `<head>` y `<body>`), esto se debe a que `base.html` si la contiene y como `index.html` hereda de base.html no tiene necesidad de la estructura base de una página `HTML`.

### Ventajas de usar herencia

- Reutilización: No repites cabeceras, footers ni menús en cada archivo.
- Mantenibilidad: Cambios globales se hacen en la plantilla base.
- Escalabilidad: Ideal para proyectos grandes con muchas vistas.
- Claridad: Separas estructura común de contenido específico.

### Buenas prácticas

- Define una estructura mínima y clara en la plantilla base.
- Usa nombres de bloques descriptivos (content, sidebar, scripts).
- Evita sobrecargar la base con lógica; mantenla como esqueleto.
- Documenta qué bloques deben sobrescribirse para que otros desarrolladores lo entiendan.

## Variables

En Jinja2, las variables son los datos que pasas desde tu aplicación Flask hacia las plantillas, y se representan dentro de `{{...}}`. Son la base para mostrar información dinámica en tu HTML.

### Cómo funcionan las Variables

En Flask defines valores y los envías al template con `render_template`. Esto ya lo vimos anteriormente:

```py
@rutas_bp.route('/')
def inicio():
    # Variable que es una Lista
    cursos = ['PHP', 'Python', 'Java', 'JavaScript', 'MySQL', 'Kotlin']
    # Variable que es un diccionario
    dato = {
        'titulo': 'Index',
        'bienvenida': '¡Saludos!'
        # agregamos la lista al diccionario
        'cursos': cursos,
        'num_cursos': len(cursos)
    }
    return render_template('index.html', data=dato)
```

Explicación: en la imagen hay dos variables (`cursos` y `dato`):

- La variable `cursos` es una `lista`.
- La variable `dato` es un `diccionario`.

En la imagen se observa que solo una variable es enviada a través del `render_template`.

La variable `dato` es se pasa al template y se le asigna el nombre de `data` y con ese nombre será utilizada en el archivo `.html` como se muestra en la siguiente imagen:

```html
<body>
    <!-- Pasamos la variable data al h1 -->
    <h1>{{ data.bienvenida }}</h1>
    
    <p>Cursos</p>
    <ul>
        <!-- Iniciamos el bucle for -->
        {% for c in data.cursos %}
        <li>{{ c }}</li>
        <!-- Terminamos el bucle for -->
        {% endfor %}
    </ul>
</body>
```

## Filtros y Funciones

En Jinja2, los filtros son funciones que transforman valores directamente en las plantillas, mientras que las funciones (macros y llamadas a funciones Python) permiten reutilizar lógica y generar contenido dinámico. Los filtros se aplican con el operador `|`, y las macros funcionan como funciones definidas dentro de las plantillas.

### Filtros

Los filtros son como “funciones rápidas” que se aplican a variables en el template.
