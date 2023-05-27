from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse(
        """
        <h1>Motor de inferencia</h1>
    """
    )


def hola_mundo(request):
    return HttpResponse(
        """
        <h1>hola mundo con Django!!!</h1>
        <h3>Soy Cristian</h3>
    """
    )


def pagina(request):
    return HttpResponse(
        """
        <h1>Página de mi WEB</h1>
        <h3>Creado por Cristian Tapia</h3>
    """
    )
