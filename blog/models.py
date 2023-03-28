from django.db import models

# Create your models here.
import os
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=30)
    hook=models.TextField(default='')
    content=models.TextField()
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload=models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}' #: 앞에 키값이 나오고
        #return self.title 타이틀 값만

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)