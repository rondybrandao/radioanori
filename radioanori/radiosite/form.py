'''
Created on 18 de abr de 2017

@author: rondy
'''

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('comentario',)

