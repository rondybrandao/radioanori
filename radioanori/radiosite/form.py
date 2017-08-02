'''
Created on 18 de abr de 2017

@author: rondy - radioanori
'''

from django import forms

from .models import Comentario, Anuncio, Attachment, ModelForm, Image
from multiupload.fields import MultiFileField


class PostForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)


class PostFormClassificado(forms.Form):
    
    titulo = forms.CharField()
    valor = forms.FloatField()
    contato = forms.CharField()
    #descricao = forms.Textarea()
    imagem = forms.FileField()
    
    class Meta:
        model = Anuncio
        
        
        #widgets={"files":forms.FileInput(attrs={'id':'files','required':True,'multiple':True})}

class FormClassificado(forms.ModelForm):
    
    class Meta:
        model = Anuncio
        fields = ['titulo',
                  'valor',
                  'contato',
                  'descricao',]
        
    files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    
    def save(self, commit=True):
        instance = super(FormClassificado, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, message=instance)
        
        return instance

class AddForm(ModelForm):
    first = MultiFileField(min_num=1, max_num=20)
    
    
    class Meta:
        model = Anuncio
        fields = ('titulo', 
                  'valor',
                  'contato',
                  'descricao', 
                  'first',)

    def save(self, commit=True):
        
        first_images = self.cleaned_data.pop('first')
        instance = super(AddForm, self).save()
        cont = 0
        for each in first_images:
           first = Image(image=each, profile=instance, cont=cont)
           cont = cont + 1
           first.save() 
    
        return instance
