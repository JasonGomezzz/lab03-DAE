from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    synopsis = models.TextField(verbose_name="Sinopsis")
    release_date = models.DateField(verbose_name="Fecha de Lanzamiento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return self.title