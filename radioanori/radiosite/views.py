from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'radiosite/index.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'radiosite/post_detail.html', {'post':post})



'''
def single_page(request):
    page = get_object_or_404(Post)
    return render(request, 'single_page.html', {'page':page})
'''