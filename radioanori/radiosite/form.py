'''
Created on 18 de abr de 2017

@author: rondy
'''

from django import forms

from .models import Comentario, Anuncio

class PostForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)


class PostFormClassificado(forms.ModelForm):
    
    class Meta:
        model = Anuncio
        fields = [
            "titulo",
            "valor",
            "descricao",
            "contato",
            "imagem",
            
        ]
        widgets={"files":forms.FileInput(attrs={'id':'files','required':True,'multiple':True})}