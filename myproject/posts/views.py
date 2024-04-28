from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(req):
    posts = Post.objects.all().order_by('-date')
    return render(req, 'posts/posts_list.html',{
        'posts':posts
    })
