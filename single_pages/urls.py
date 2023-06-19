from django.urls import path
from . import views

from django.urls import path
from . import views

# urlpatterns=[
#     # path('', views.login, name='login'),  # 로그인 페이지
#     path('signup/', views.signup, name='signup'),  # 회원가입 페이지
#     path('', views.login_view, name='login'),
# ]

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]