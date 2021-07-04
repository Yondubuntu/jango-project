from django.shortcuts import render
from .models import Post 

def index(request): 
    posts = Post.objects.all().order_by('-pk')

    return render  ( 
        request, 

        'blog/index.html',
        { 
            'posts': posts, 
        }
    )
# Create your views here.


def single_post_page(request, pk):  
 
    post = Post.objects.get(pk=pk)
    return render(       
        request, # render 템플릿 안에 blog 안에 html 파일 찾게 하는 함수 
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
