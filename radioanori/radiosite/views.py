from django.shortcuts import render, get_object_or_404
from .models import Post, Megasena, Anuncio, Image
from .form import PostForm, FormClassificado, AddForm
from django.shortcuts import redirect
from radiosite import form
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.db.models import Q

def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post_destaque_1 = get_object_or_404(Post, pk=4)
    post_destaque_2 = get_object_or_404(Post, pk=3)
    post_politica_1 = get_object_or_404(Post, pk=1)
    post_politica_2 = get_object_or_404(Post, pk=2)
    post_politica_3 = get_object_or_404(Post, pk=3)
    post_policia_1 = get_object_or_404(Post, pk=5)
    post_policia_2 = get_object_or_404(Post, pk=7)
    post_policia_3 = get_object_or_404(Post, pk=5)
    post_cotidiano_1 = get_object_or_404(Post, pk=6)
    post_cotidiano_2 = get_object_or_404(Post, pk=4)
    post_esporte_1 = get_object_or_404(Post, pk=8)
    anuncio_01 = get_object_or_404(Anuncio, pk=1)
    anuncio_02 = get_object_or_404(Anuncio, pk=1)
    anuncio_03 = get_object_or_404(Image, pk=1)
    anuncio_04 = get_object_or_404(Anuncio, pk=1)
    anuncio_05 = get_object_or_404(Anuncio, pk=1)
    anuncio_06 = get_object_or_404(Anuncio, pk=1)
    anuncio_07 = get_object_or_404(Anuncio, pk=1)
    anuncio_08 = get_object_or_404(Anuncio, pk=1)
    anuncio_09 = get_object_or_404(Anuncio, pk=1)
    anuncio_10 = get_object_or_404(Anuncio, pk=1)
    return render(request, 'radiosite/index.html', {
                                                    'anuncio_01':anuncio_01,
                                                    'anuncio_02':anuncio_02,
                                                    'anuncio_03':anuncio_03,
                                                    'anuncio_04':anuncio_04,
                                                    'anuncio_05':anuncio_05,
                                                    'anuncio_06':anuncio_06,
                                                    'anuncio_07':anuncio_07,
                                                    'anuncio_08':anuncio_08,
                                                    'anuncio_09':anuncio_09,
                                                    'anuncio_10':anuncio_10,
                                                    'post_destaque_1':post_destaque_1,
                                                    'post_destaque_2':post_destaque_2,
                                                    'post_policia_1':post_policia_1,
                                                    'post_policia_2':post_policia_2,
                                                    'post_policia_3':post_policia_3,                                          
                                                    'post_politica_1':post_politica_1,
                                                    'post_politica_2':post_politica_2,
                                                    'post_politica_3':post_politica_3,
                                                    'post_cotidiano_1':post_cotidiano_1,
                                                    'post_cotidiano_2':post_cotidiano_2,
                                                    'post_esporte_1':post_esporte_1,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'radiosite/post_detail.html', {'post':post})

def em_construcao(request):
    return render(request, 'radiosite/emconstrucao.html')

def anori(request):
    return render(request, 'radiosite/anori.html')

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

'''
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


def loteria(request):
    
    if request.method=="POST":
        n_usuario = request.POST.getlist('pesquisa')
        nUsuario = n_usuario
        return redirect(megasena(nUsuario))
        #return redirect(megasena)
    return render(request, 'radiosite/loteria.html')

def megasena(request):
    megasena_resposta = {}
    num_usuario = request.POST.getlist('pesquisa')
    encontrado = []
    lista_resultado_db = []    
    lista_consurso = []
    cont_concurso = {}
    concursos = []
    lista_megasena = []
    if request.method=="POST" and (len(num_usuario) == 6 or len(num_usuario) == 0):      
        for u in num_usuario:
            megasena = Megasena.objects.filter(Q(num_1=u) | Q(num_2=u) | Q(num_3=u) | Q(num_4=u) | Q(num_5=u) | Q(num_6=u)).distinct('num_concurso')                                             
            for m in megasena:
                lista_resultado_db = m.num_1, m.num_2, m.num_3, m.num_4, m.num_5, m.num_6                                
                
                if u in lista_resultado_db:  
                    lista_consurso.append(m.num_concurso)
                    lista_megasena.append(m)
                    
                    if m.num_concurso not in cont_concurso:
                        cont_concurso[m.num_concurso] = 1
                    else:
                        cont_concurso[m.num_concurso] += 1
                                
        for k, c in cont_concurso.items():
            for m in lista_megasena:
                if c > 3 and k == m.num_concurso:
                    megasena_resposta[m] = c + 1
                    
    
    print(concursos, cont_concurso.items())
    print("num_usuario:", num_usuario)  
    return render(request, 'radiosite/loteria.html', {'megasena_resposta':megasena_resposta,
                                                   'escolhidas':num_usuario,
                                                   'encontrado':encontrado})
def post_anuncio(request, pk):
    instance = get_object_or_404(Anuncio, pk=pk)
    #imagem = get_object_or_404(Anuncio_imagens, pk=_imagem_id)
    return render(request, 'radiosite/anuncio_teste.html', {'instance':instance})
                                                          

def post_anuncio_detalhe(request, pk):
    #image = get_object_or_404(Image, pk=pk)
    anuncio_01 = get_object_or_404(Anuncio, pk=pk)
    image = Image.objects.filter(pk=pk)
    return render(request, 'radiosite/anuncio-detail.html', {
                                                             'anuncio_01':anuncio_01,
                                                             'image':image})

def anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    foto = Image.objects.filter(profile=pk)
    return render(request, 'radiosite/anuncio.html', {'foto':foto,
                                                      'anuncio':anuncio})
    
def post_classificados(request):
    form = FormClassificado(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        
        return HttpResponseRedirect('classificados')
    context = {
        "form":form,
        
        
    }
    return render(request, "radiosite/form_classificado.html", context)

def add_form(request, *callback_args, **callback_kwargs): 
    
    if request.method == "POST": 
        
        form = AddForm(request.POST, request.FILES)

        if form.is_valid(): 
            profile = form.save(commit=False) 
            profile.profile = request.user
            profile.save()
            return redirect('anuncio', pk=profile.pk)
        
    else: 
        form = AddForm() 
    return render(request, 'radiosite/formFormulario.html', {'form': form})

def form_detail(request, pk):

    profile = get_object_or_404(Anuncio, pk=pk)
    foto = Image.objects.filter(profile=pk)
    
    return render(request, 'radiosite/form_detail.html', {'profile':profile,
                                                     'foto':foto})

def api_google_maps(request):
    
    return render(request, 'radiosite/api_google_maps.html')


class ContactView(CreateView):

    model = Anuncio
    form_class = FormClassificado
    template_name = 'radiosite/form_classificado.html'
    success_url = '?success'
