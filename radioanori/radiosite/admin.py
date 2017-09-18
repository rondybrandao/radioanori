from django.contrib import admin
from .models import Post, Anuncio, Image
from django import forms


admin.site.register(Post)
admin.site.register(Anuncio)
admin.site.register(Image)
