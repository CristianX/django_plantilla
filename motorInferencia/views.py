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
    html = """
        <h1>Motor de inferencia</h1>
        <p>Años hasta el 2050: </p>
        <ul>
    """
    year = 2021

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    return HttpResponse(layout + html)


def hola_mundo(request):
    return HttpResponse(
        layout
        + """
        <h1>hola mundo con Django!!!</h1>
        <h3>Soy Cristian</h3>
    """
    )


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("contacto", nombre="Cristian", apellido="Tapia")

    return HttpResponse(
        layout
        + """
        <h1>Página de mi WEB</h1>
        <h3>Creado por Cristian Tapia</h3>
    """
    )


def contacto(request, nombre="", apellido=""):
    html = ""
    if nombre and apellido:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)
