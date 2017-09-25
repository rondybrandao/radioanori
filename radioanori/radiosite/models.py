from django.db import models
from django.utils import timezone
import os
from django.forms.models import ModelForm
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _

class Comentario(models.Model):
    author = models.ForeignKey('auth.User')
    comentario = models.CharField(max_length=200, default='SOME STRING')
    
class Post(models.Model):
    
    CATEGORIA_CHOICES = (
        ('policial', 'Policial'),
        ('politica', 'Politica'),
        ('cultura', 'Cultura'),
        ('esporte', 'Esporte'),
        ('cotidiano', 'Cotidiano'),
    )
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='SOME STRING')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    imagem = models.FileField(null=True)
    #comentario = models.ManyToManyField(Comentario)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Loteria(models.Model):
   
    concurso_loteria = models.CharField(max_length=50)
    data_loteria = models.CharField(max_length=50)
    acerto_loteria = models.CharField(max_length=50)
    entrada_usuario = models.CharField(max_length=50)
    result = models.CharField(max_length=200)
    def search_result(self):
        # valores capturados do usuario
        numeros_procurados = []
        numeros_procurados.append(self.entrada_usuario)
        entrada_usuario_string = str(numeros_procurados).strip().split()
        #entrada_usuario_string = entrada_usuario.
        print(entrada_usuario_string)
        #print(self.entrada_usuario)
        
        # abri arquivo loteria.txt e relaciona dta com valores
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'lotofacil.txt')
        f=open(filename)
        
        dic = {}
        for linha in f:
            # y = str(linha.strip().split())   
            y = str(linha.split())
            
            dic[y[1:20]] = y[20:107]
            # dic[y[0:2]] = y[4:19]
        
        f.close()
        v_encontrado = []
        value_encontrado = []
        resultado_usuario = {}
        cont_key_concurso = {}
       
        b = "'',"
        for key_dic, value_dic in dic.items():
            #key_dic = key_dic.strip().split()
            #print(key_dic)
            # remove aspas e vigula
            for i in range(0, len(b)):
                value_dic = str(value_dic).replace(b[i], "")
                key_dic = str(key_dic).replace(b[i], "")
                #print(key_dic)
            
            #print(key_dic.split())

            for j in value_dic.split():
                
                for w in self.entrada_usuario:
                    if w in j:
                        #v_encontrado.append(key_dic[0:18])
                        resultado_usuario[key_dic.split().pop(0)] = key_dic.split().pop(1)                        
                        value_encontrado.append(value_dic[0:])
                        #colocar um contador aqui para numero do concurso
                        if key_dic.split().pop(0) not in cont_key_concurso:
                            cont_key_concurso[key_dic.split().pop(0)] = 1
                        else:
                            cont_key_concurso[key_dic.split().pop(0)] += 1
                        #print(w, j)
                        #print(key_dic.split().pop(0), key_dic.split().pop(1))
                        
        '''                
        v = {}
        concurso = {}
        print(resultado_usuario)
        for chave_concurso, valor_data in resultado_usuario.items():
            if chave_concurso not in v: 
                v[chave_concurso] = 1
                concurso[valor_data] = 1
                #print(v[chave_concurso])
            else:
                v[chave_concurso] += 1
                concurso[valor_data] += 1
                
        '''       
        print(cont_key_concurso.items())
        #print(v.items())

        #chaves contendo + 2,3,4,5,6 elementos
        data_encontrada_11 = []
        concurso_encontrado_11 = []
        acerto_encontrado_11 = []
        r=[]
        #print(concurso)
        #print(v)
        for v_key, value_v in cont_key_concurso.items():
            #print(v_key)
            #for concurso_key, concurso_value in concurso.items():    
            if value_v == 11:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)
                
                r.append(v_key)
                r.append(resultado_usuario[v_key])
                r.append(value_v)
                
            if value_v == 12:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)
                
                
                r.append(v_key)
                r.append(resultado_usuario[v_key])
                r.append(value_v)
                
                
            if value_v == 13:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)        
                
                r.append(v_key + resultado_usuario[v_key] + value_v)
            
            if value_v == 14:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)        
                
                r.append(v_key + resultado_usuario[v_key] + value_v)
                
            if value_v == 15:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)        
                
                r.append(v_key + resultado_usuario[v_key] + value_v)
                    
        self.concurso_loteria = concurso_encontrado_11
        self.data_loteria = data_encontrada_11
        self.acerto_loteria = acerto_encontrado_11
        self.result = r

class Megasena(models.Model):
   
    concurso_loteria = models.CharField(max_length=50)
    data_loteria = models.CharField(max_length=50)
    acerto_loteria = models.CharField(max_length=50)
    entrada_usuario = models.CharField(max_length=50)
    result = models.CharField(max_length=200)
    def search_result(self):
        # valores capturados do usuario
        numeros_procurados = []
        numeros_procurados.append(self.entrada_usuario)
        entrada_usuario_string = str(numeros_procurados).strip().split()
        #entrada_usuario_string = entrada_usuario.
        print(entrada_usuario_string)
        #print(self.entrada_usuario)
        
        # abri arquivo loteria.txt e relaciona dta com valores
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'megasena.txt')
        f=open(filename)
        
        dic = {}
        for linha in f:
            # y = str(linha.strip().split())   
            y = str(linha.split())
            
            dic[y[1:20]] = y[20:107]
            # dic[y[0:2]] = y[4:19]
        
        f.close()
        v_encontrado = []
        value_encontrado = []
        resultado_usuario = {}
        cont_key_concurso = {}
       
        b = "'',"
        for key_dic, value_dic in dic.items():
            #key_dic = key_dic.strip().split()
            #print(key_dic)
            # remove aspas e vigula
            for i in range(0, len(b)):
                value_dic = str(value_dic).replace(b[i], "")
                key_dic = str(key_dic).replace(b[i], "")
                #print(key_dic)
            
            #print(key_dic.split())

            for j in value_dic.split():
                
                for w in self.entrada_usuario:
                    if w in j:
                        #v_encontrado.append(key_dic[0:18])
                        resultado_usuario[key_dic.split().pop(0)] = key_dic.split().pop(1)                        
                        value_encontrado.append(value_dic[0:])
                        #colocar um contador aqui para numero do concurso
                        if key_dic.split().pop(0) not in cont_key_concurso:
                            cont_key_concurso[key_dic.split().pop(0)] = 1
                        else:
                            cont_key_concurso[key_dic.split().pop(0)] += 1
                        #print(w, j)
                        #print(key_dic.split().pop(0), key_dic.split().pop(1))
                        
        '''                
        v = {}
        concurso = {}
        print(resultado_usuario)
        for chave_concurso, valor_data in resultado_usuario.items():
            if chave_concurso not in v: 
                v[chave_concurso] = 1
                concurso[valor_data] = 1
                #print(v[chave_concurso])
            else:
                v[chave_concurso] += 1
                concurso[valor_data] += 1
                
        '''       
        print(cont_key_concurso.items())
        #print(v.items())

        #chaves contendo + 2,3,4,5,6 elementos
        data_encontrada_11 = []
        concurso_encontrado_11 = []
        acerto_encontrado_11 = []
        r=[]
        #print(concurso)
        #print(v)
        for v_key, value_v in cont_key_concurso.items():
            #print(v_key)
            #for concurso_key, concurso_value in concurso.items():    
            if value_v == 2:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)
                
                r.append(v_key)
                r.append(resultado_usuario[v_key])
                r.append(value_v)
                
            if value_v == 3:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)
                
                
                r.append(v_key)
                r.append(resultado_usuario[v_key])
                r.append(value_v)
                
                
            if value_v == 4:
                for i in range(0, len(b)):
                    v_key = str(v_key).replace(b[i], "")
                    value_v = str(value_v).replace(b[i], "")
                
                concurso_encontrado_11.append(v_key)
                data_encontrada_11.append(resultado_usuario[v_key])
                acerto_encontrado_11.append(value_v)        
                
                r.append(v_key + resultado_usuario[v_key] + value_v)
                    
        self.concurso_loteria = concurso_encontrado_11
        self.data_loteria = data_encontrada_11
        self.acerto_loteria = acerto_encontrado_11
        self.result = r

class Anuncio_imagens(models.Model):
    #anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    imagem = models.FileField(upload_to="files/%Y/%m/%d")
     
class Anuncio(models.Model):
    #user=models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='anuncio')
    
    titulo = models.CharField(max_length=30)
    valor = models.FloatField(null=True, blank=True)
    contato = models.CharField(max_length=30, null=True,)
    descricao = models.TextField()
    imagem = models.FileField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    
    def __unicode__(self):
        return self.titulo 
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ["-data"]

    
class Attachment(models.Model):
    message = ForeignKey(Anuncio, verbose_name=_('Anuncio'), null=True)
    file = models.FileField(upload_to='attachments')

class Image(models.Model):
    image = models.FileField()
    profile = models.ForeignKey(Anuncio)
    cont = models.IntegerField()
    
    def __str__(self):
        return self.profile.titulo

    def contador(self):
        self.cont = self.cont + 1
        return self.cont
        
class AnuncioForm(ModelForm):
    
    class Meta:
        model = Anuncio
        fields = '__all__'
