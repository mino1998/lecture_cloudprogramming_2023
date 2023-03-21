from django.shortcuts import render
from . models import Post

def index(request):
    posts=Post.objects.all().order_by('-pk')  #created_at 넣으면 생성시간 순서대로겠지, -를 붙이면 내림차순이다.

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )

def single_post_page(request, pk):
    post=Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )