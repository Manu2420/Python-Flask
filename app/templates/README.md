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
