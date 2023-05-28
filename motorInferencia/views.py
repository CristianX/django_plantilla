from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
<h1>Sitio Web con Django    | Cristian Tapia </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):
    """
    html = ""
        <h1>Motor de inferencia</h1>
        <p>Años hasta el 2050: </p>
        <ul>
    ""

    year = 2021

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"
    """

    year = 2021
    hasta = range(year, 2051)

    nombre = "Cristian Tapia"
    lenguajes = ["JavaScript", "Python", "PHP", "C"]
    # lenguajes = []

    return render(
        request,
        "index.html",
        {
            "title": "Motor de Inferencia",
            "mi_variable": "código que está en la vista",
            "nombre": nombre,
            "lenguajes": lenguajes,
            "years": hasta,
        },
    )


def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("contacto", nombre="Cristian", apellido="Tapia")

    return render(request, "pagina.html")


def contacto(request, nombre="", apellido=""):
    html = ""
    if nombre and apellido:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)
