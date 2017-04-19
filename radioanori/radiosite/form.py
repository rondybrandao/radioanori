'''
Created on 18 de abr de 2017

@author: rondy
'''

from django import forms

from .models import Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)

