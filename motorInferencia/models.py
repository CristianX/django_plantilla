from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Se pone automáticamente cuando se crea el registro
    update_at = models.DateTimeField(
        auto_now=True
    )  # Se pone automáticamente cuando se edita el registro


class CategorY(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_at = models.DateTimeField()
