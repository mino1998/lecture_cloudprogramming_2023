from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from bookmark.views import BookmarkLV, BookmarkDV, create_bookmark, delete_bookmark
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('',BookmarkLV.as_view(), name='index'),
    path('<int:pk>/',BookmarkDV.as_view(), name='detail'),
    path('create/', create_bookmark, name='create_bookmark'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('<int:pk>/delete/', delete_bookmark, name='delete_bookmark')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)