from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Loteria, Megasena, Anuncio, Attachment, Image
from .form import PostForm, FormClassificado, AddForm
from django.shortcuts import redirect
from radiosite import form
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    anuncio_01 = get_object_or_404(Anuncio, pk=12)
    anuncio_02 = get_object_or_404(Anuncio, pk=12)
    anuncio_03 = get_object_or_404(Image, pk=14)
    anuncio_04 = get_object_or_404(Anuncio, pk=10)
    anuncio_05 = get_object_or_404(Anuncio, pk=9)
    anuncio_06 = get_object_or_404(Anuncio, pk=7)
    anuncio_07 = get_object_or_404(Anuncio, pk=6)
    anuncio_08 = get_object_or_404(Anuncio, pk=6)
    anuncio_09 = get_object_or_404(Anuncio, pk=6)
    anuncio_10 = get_object_or_404(Anuncio, pk=6)
    return render(request, 'radiosite/index.html', {'posts':posts, 
                                                    'anuncio_01':anuncio_01,
                                                    'anuncio_02':anuncio_02,
                                                    'anuncio_03':anuncio_03,
                                                    'anuncio_04':anuncio_04,
                                                    'anuncio_05':anuncio_05,
                                                    'anuncio_06':anuncio_06,
                                                    'anuncio_07':anuncio_07,
                                                    'anuncio_08':anuncio_08,
                                                    'anuncio_09':anuncio_09,
                                                    'anuncio_10':anuncio_10,})

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
            return redirect('form_detail', pk=profile.pk)
        
    else: 
        form = AddForm() 
    return render(request, 'radiosite/formFormulario.html', {'form': form})

def form_detail(request, pk):
    profile = get_object_or_404(Anuncio, pk=pk)
    foto = Image.objects.filter(profile=pk)
    
    return render(request, 'radiosite/form_detail.html', {'profile':profile,
                                                     'foto':foto})

class ContactView(CreateView):
    model = Anuncio
    form_class = FormClassificado
    template_name = 'radiosite/form_classificado.html'
    success_url = '?success'
