from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os
from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name=models.CharField(max_length=50, unique=True) #유일한 값을 가지게 하는 유니크
    slug=models.SlugField(max_length=200,unique=True, allow_unicode=True) #slugfield는 한글을 허용하지 않으나, allow값을 true로 하면 사용 가능하다.
    ##slug란 무엇인가? pk or 글의 일부가 url에 일부에 들어갈 수 있다.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

class Post(models.Model):
    title=models.CharField(max_length=30)
    hook=models.TextField(default='')
    content=models.TextField()
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload=models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, null=False, on_delete=models.CASCADE) #user class가 없으니까 쟝고에 user라는 모델 불러올거에요~
    #cascade는 계단식이라 사라지면 전부 사라지게 만든다 이말이에요

    category=models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) #기본 카테고리로 가던가, 카테고리 없음으로 가려면 set_null, 왜냐면 null 이 true니까
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return f'[{self.pk}] {self.title}::{self.author}' #: 앞에 키값이 나오고
        #return self.title 타이틀 값만

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)