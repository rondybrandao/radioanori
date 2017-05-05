from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Loteria, Megasena
from .form import PostForm
from django.shortcuts import redirect
from radiosite import form
from django.core.files.uploadedfile import UploadedFile


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'radiosite/index.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'radiosite/post_detail.html', {'post':post})

def post_comentario(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post_comentario(form)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return redirect('post_detail', pk=post.pk)

def loteria(request):
    return render(request, 'radiosite/loteria.html')

def pesquisar_lotofacil(request):
    if request.method == "POST":
        
        entrada = Loteria(request.POST)
        entrada.entrada_usuario = request.POST.getlist('pesquisa')
        entrada.search_result()
        
        con_n_concurso = entrada.concurso_loteria
        con_data_sorteio = entrada.data_loteria
        con_qnt_acerto = entrada.acerto_loteria
        
        consulta_concurso = [con_n_concurso, con_data_sorteio, con_qnt_acerto]
        
        result = entrada.result
        
        
        return render(request, 'radiosite/lotofacil.html',  {'con_n_concurso':con_n_concurso, 'entrada':entrada,
                                                             'con_data_sorteio':con_data_sorteio, 'con_qnt_acerto':con_qnt_acerto,
                                                             'consulta_concurso':consulta_concurso,
                                                             'result':result})
    else:
        entrada = Loteria()  
    return render(request, 'radiosite/lotofacil.html', {'entrada': entrada})
    
def pesquisar_megasena(request):
    if request.method == "POST":
        
        entrada = Megasena(request.POST)
        entrada.entrada_usuario = request.POST.getlist('pesquisa')
        entrada.search_result()
        
        con_n_concurso = entrada.concurso_loteria
        con_data_sorteio = entrada.data_loteria
        con_qnt_acerto = entrada.acerto_loteria
        
        consulta_concurso = [con_n_concurso, con_data_sorteio, con_qnt_acerto]
        
        result = entrada.result
        
        
        return render(request, 'radiosite/megasena.html',  {'con_n_concurso':con_n_concurso, 'entrada':entrada,
                                                             'con_data_sorteio':con_data_sorteio, 'con_qnt_acerto':con_qnt_acerto,
                                                             'consulta_concurso':consulta_concurso,
                                                             'result':result})
    else:
        entrada = Megasena()  
    return render(request, 'radiosite/megasena.html', {'entrada': entrada})


def pesquisar_megasena_result(request):
    if request.method == "POST":
        
        entrada = Megasena(request.POST)
        entrada.entrada_usuario = request.POST.getlist('pesquisa')
        entrada.search_result()
        
        con_n_concurso = entrada.concurso_loteria
        con_data_sorteio = entrada.data_loteria
        con_qnt_acerto = entrada.acerto_loteria
        
        consulta_concurso = [con_n_concurso, con_data_sorteio, con_qnt_acerto]
        
        result = entrada.result
        
        
        return render(request, 'radiosite/megasena-result.html',  {'con_n_concurso':con_n_concurso, 'entrada':entrada,
                                                             'con_data_sorteio':con_data_sorteio, 'con_qnt_acerto':con_qnt_acerto,
                                                             'consulta_concurso':consulta_concurso,
                                                             'result':result})
    else:
        entrada =Megasena()  
    return render(request, 'radiosite/megasena-result.html', {'entrada': entrada})

'''     
def search_result(self):
        
        # valores capturados do usuario
        #numeros_procurados = '{}'.format(self.search_input.text)
        numeros_procurados = self
        #print(numeros_procurados)
        # abri arquivo loteria.txt e relaciona dta com valores
        #f = open('lotofacil_teste2.txt', 'rb')
        uploaded = UploadedFile(open('teste.txt', 'rb'), 'teste.txt')
        uploaded.close()
        uploaded.open('r')
        #print(f)
        dic = {}
        for linha in csv.reader(uploaded.file):
            # y = str(linha.strip().split())
            # print(y)
            y = str(linha.split())
            # print(y)
            dic[y[1:18]] = y[20:107]
            # dic[y[0:2]] = y[4:19]
        #print(dic)
        #f.close()
        v_encontrado = []
        value_encontrado = []
        b = "'',"
        for key_dic, value_dic in dic.items():
            # remove aspas e vigula
            for i in range(0, len(b)):
                value_dic = str(value_dic).replace(b[i], "")
                key_dic = str(key_dic).replace(b[i], "")

            for j in value_dic.split():
                for w in numeros_procurados.strip().split():
                    if w in j:
                        v_encontrado.append(key_dic[0:18])
                        value_encontrado.append(value_dic[0:])

        v = {}
        for p in v_encontrado:
            if p not in v:
                v[p] = 1
            else:
                v[p] += 1
        print(v_encontrado)
        print(v.items())

        #chaves contendo + 2,3,4,5,6 elementos
        k_encontrado=[]
        k_encontrado_12=[]
        k_encontrado_13 = []
        
        for key_v , value_v in v.items():
            if value_v == 2:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado.append(key_v)

            elif value_v == 3:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado_12.append(key_v)

            elif value_v == 4:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado_13.append(key_v)
        
        mysorteio={'sorteio':k_encontrado}
        
        return mysorteio;   


def pesquisar_lotofacil(request):
    ctx = {'mysorteio':search_result(request)}
    return render(request, 'radiosite/loteria.html', ctx)
    
'''