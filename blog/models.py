from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()

    created_at=models.DateTimeField()
    updated_at=models.DateTimeField(auto_now=True)
    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}' #: 앞에 키값이 나오고
        #return self.title 타이틀 값만