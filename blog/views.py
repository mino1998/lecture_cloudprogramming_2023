import os.path

from django.shortcuts import render
from . models import Post, Category, Tag
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model=Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(PostList, self).get_context_data()
        context['categories']=Category.objects.all() #모든 카테고리 목록을 다 넣어버림
        context['no_category_post_count']=Post.objects.filter(category=None).count() #카테고리가 없는 글들은 어떻게 처리할까? 카테고리가 None인 애들을 체크하자
        return context

class PostDetail(DetailView):
    model=Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(PostDetail, self).get_context_data()
        context['categories']=Category.objects.all() #모든 카테고리 목록을 다 넣어버림
        context['no_category_post_count']=Post.objects.filter(category=None).count() #카테고리가 없는 글들은 어떻게 처리할까? 카테고리가 None인 애들을 체크하자
        return context
def categories_page(request, slug):
    if slug=='no-category':
        category='미분류'
        post_list=Post.objects.filter(category=None)
    else:
        category=Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    context={
        'categories':Category.objects.all(),
        'no_category_post_count':Post.objects.filter(category=None).count(),
        'category':category,
        'post_list':post_list,
    }
    return render(request, 'blog/post_list.html',context)

def tag_page(request, slug):
    tag=Tag.objects.get(slug=slug)
    post_list=tag.post_set.all()
    context={
        'tag': tag,
        'categories':Category.objects.all(),
        'post_list':post_list,
        'no_category_count':Post.objects.filter(category=None).count(),
    }
    return render(request, 'blog/post_list.html',context)

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