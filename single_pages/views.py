from django.shortcuts import render
from blog.models import Post
def main(request):
    recent_post=Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/main.html',
        {
            'recent_posts':recent_post
        }
    )
