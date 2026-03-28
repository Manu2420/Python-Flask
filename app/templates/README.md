# Plantillas

Las plantillas `Jinja2` + `HTML` son el “motor de vistas” de `Flask`: permiten escribir páginas `HTML` que se vuelven dinámicas, usando `variables`, `bucles`, `condicionales`, `herencia` y más, todo desde el mismo archivo `.html`.

## ¿Dónde se crean las plantillas?

`Flask` busca automáticamente las plantillas en una carpeta llamada `templates` al mismo nivel que tu archivo principal (`app.py`, `run.py`, etc.):

```text
mi_proyecto/
├── app.py
├── routes/
│   └── rutas.py
└── templates/          ← aquí van tus HTML + Jinja2
    ├── base.html
    ├── index.html
    └── usuarios.html
```
