from django.contrib import admin

from filmes.models import Movie, Actor


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("create_date","name", "age")
    list_editable = ("age",)