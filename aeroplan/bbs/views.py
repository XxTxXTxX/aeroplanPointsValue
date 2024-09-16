from django.shortcuts import render
from django.http import HttpResponse, Http404
from bbs.models import Post

# Create your views here.

def get_posts(request):
    posts = Post.objects.all
    return render(request, 'post/index.html', {'posts': posts})