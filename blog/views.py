from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model=Post

class PostDetail(DetailView):
    model=Post
# def index(request):
#     posts=Post.objects.all().order_by('-pk')  #created_at 넣으면 생성시간 순서대로겠지, -를 붙이면 내림차순이다.
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )

# def single_post_page(request, pk):
#     post=Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post':post,
#         }
#     )