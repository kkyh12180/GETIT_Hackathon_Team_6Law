from django.db import models
from django.conf import settings
import os
# Create your models here.

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/ask/category/{self.slug}/'

    class Meta:
        verbose_name_plural='Categories'   

class Post(models.Model) : 
    title = models.CharField(max_length=30)
    content = models.TextField()

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.SET_NULL)

    # pk : 기본키
    def __str__(self) :
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self) :
        return f'/ask/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

class Answer(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def  __str__(self) :
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'