from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    actor = models.ManyToManyField("Actor", verbose_name="Ator")

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __str__(self):
        return self.name
class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    age = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
        ordering = ("name",)

    def __str__(self):
        return self.name

