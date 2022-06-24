from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Crear el modelo Post en nuesta BD para guardar los posts

class Post(models.Model):
    """class representing post"""
    maquinaria = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='images', null=True, blank = True)
    detalle = RichTextField()

    class Meta:
        ordering = ['-fecha']

def __str__(self):
    return self.maquinaria
