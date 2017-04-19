from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .form import PostForm
from django.shortcuts import redirect
from radiosite import form

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
'''
def single_page(request):
    page = get_object_or_404(Post)
    return render(request, 'single_page.html', {'page':page})
'''