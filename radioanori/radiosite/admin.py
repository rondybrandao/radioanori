from django.contrib import admin
from .models import Post, Anuncio, Image
from django import forms

class PostAdmin(admin.ModelAdmin):
    list_display = ['pk',
                    'categoria',
                    'author',
                    'title',
                    'text',
                    'imagem',]

admin.site.register(Post, PostAdmin)
admin.site.register(Anuncio)
admin.site.register(Image)
