from django.shortcuts import render
from blog.models import Post
# def main(request):
#     recent_post=Post.objects.order_by('-pk')[:3]
#     return render(
#         request,
#         'single_pages/main.html',
#         {
#             'recent_posts':recent_post
#         }
#     )

from django.shortcuts import render, redirect
# from .models import User
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # Perform authentication
#         if username and password:
#             try:
#                 user = User.objects.get(username=username, password=password)
#                 # Successful authentication, redirect to second app
#                 return redirect('/blog/')
#             except User.DoesNotExist:
#                 # Authentication failed
#                 error_message = 'Authentication failed.'
#                 return render(request, 'single_pages/login.html', {'error_message': error_message})
#
#     # Render login page
#     return render(request, 'single_pages/login.html')
#
# def signup(request):
#     if request.method == 'POST':
#         # 회원가입 폼에서 전달된 데이터를 받아옴
#         username = request.POST.get('signup-username')
#         password = request.POST.get('signup-password')
#
#         # 회원 정보 생성
#         user = User(username=username, password=password)
#         user.save()
#
#         # 회원가입 후 로그인 페이지로 리다이렉트
#         return redirect('login/')
#
#     return render(request, 'single_pages/signup.html')
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/blog/')  # 로그인 성공 시 리디렉션할 URL
#         else:
#             error_message = 'Authentication failed.'
#             return render(request, 'single_pages/login.html', {'error_message': error_message})
#     else:
#         return render(request, 'single_pages/login.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/bookmark/')
        else:
            return render(request, 'single_pages/login.html', {'error': 'Authentication failed.'})
    else:
        return render(request, 'single_pages/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'single_pages/signup.html', {'success': True})
        else:
            return render(request, 'single_pages/signup.html', {'error': 'Signup failed.'})
    else:
        form = UserCreationForm()
        return render(request, 'single_pages/signup.html', {'form': form})