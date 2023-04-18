import os.path
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from . models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm

class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title', 'hook', 'content', 'head_image', 'file_upload', 'category']
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(PostCreate, self).get_context_data()
        context['categories']=Category.objects.all() #모든 카테고리 목록을 다 넣어버림
        context['no_category_post_count']=Post.objects.filter(category=None).count() #카테고리가 없는 글들은 어떻게 처리할까? 카테고리가 None인 애들을 체크하자
        return context
    def test__func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user=self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author=current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog')

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
        context['comment_form']=CommentForm
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

class PostUpdate(LoginRequiredMixin, UpdateView):
    model=Post
    fields = ['title', 'hook', 'content', 'head_image', 'file_upload', 'category', 'tag']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user==self.get_object().author: #post method로 들어오면 object get해서 유저가 같은지 확인하자
            return super(PostUpdate,self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionError #아니면 return redirect('/blog/') 이렇게 넣어도 되지만, 예외적상황, 잘못된 상황이라면 에러코드로 표시하면 확인하기 편함->http status code

    template_name = "blog/post_form_update.html"

def add_comment(request, pk):
    if request.user.is_authenticated:
        post=get_object_or_404(Post, pk=pk)

        if request.method=='POST':
            comment_form=CommentForm(request.POST)
            if comment_form.is_valid():
                comment=comment_form.save(commit=False)
                comment.post=post
                comment.author=request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionError


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