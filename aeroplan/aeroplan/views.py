from django.shortcuts import render
from django.http import HttpResponse, Http404
from bbs.models import Post


# Create view

def hello(request):
    return HttpResponse("Hello dude whats up XD")

def get_posts(request):
    posts = Post.objects.all
    return render(request, 'post/index.html', {'posts': posts})

def get_posts_if_404(request, title):
    post = get_object_or_404(Post, title=title)
    return render(request, 'post/detail.html', {'post': post})