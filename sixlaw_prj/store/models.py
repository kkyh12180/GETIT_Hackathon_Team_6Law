from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model) : 
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # pk : 기본키
    def __str__(self) :
        return f'[{self.pk}] {self.title}::{self.author}'

    def get_absolute_url(self) :
        return f'/store/{self.pk}/'