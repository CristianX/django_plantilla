"""
URL configuration for mdmq_motor_inferencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importar app con mis vistas
import motorInferencia.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", motorInferencia.views.index, name="index"),
    path("inicio/", motorInferencia.views.index, name="inicio"),
    path("hola-mundo/", motorInferencia.views.hola_mundo, name="hola_mundo"),
    path("pagina-pruebas/", motorInferencia.views.pagina, name="pagina"),
    path("pagina-pruebas/<int:redirigir>", motorInferencia.views.pagina, name="pagina"),
    path("contacto/", motorInferencia.views.contacto, name="contacto"),
    path("contacto/<str:nombre>/", motorInferencia.views.contacto, name="contacto"),
    path("contacto/<str:nombre>/<str:apellido>/", motorInferencia.views.contacto, name="contacto"),
    path("crear-articulo/<str:title>/<str:content>/<str:public>/", motorInferencia.views.crear_articulo, name="crear_articulo"),
    path("articulo/", motorInferencia.views.articulo, name="articulo"),
    path("editar-articulo/<int:id>", motorInferencia.views.editar_articulo),
    path("articulos", motorInferencia.views.articulos, name="articulos"),
    path("borrar-articulo/<int:id>", motorInferencia.views.borrar_articulo, name="borrar"),
    path("save-article/", motorInferencia.views.save_article, name="save"),
    path("create-article/", motorInferencia.views.create_article, name="create"),
    path("create-full-article/", motorInferencia.views.create_full_article, name="create_full"),
]
