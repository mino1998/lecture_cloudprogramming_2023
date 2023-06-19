from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tag_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('<int:pk>/add_comment/', views.add_comment),
    #path('', views.index),
    #path('<int:pk>/', views.single_post_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)