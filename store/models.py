from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
'''
    필요 기능
        주점 이름
        주점 소개
        주소
        리뷰
'''

class Store(models.Model) : 
    title = models.CharField(max_length=30, unique=True)
    address = models.TextField(blank=False) 
    content = models.TextField()
    table = models.IntegerField()
    # Save Image
    head_image = models.ImageField(upload_to='store/images/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # pk : 기본키
    def __str__(self) :
        return f'[{self.pk}] {self.title}::{self.author}'

    def get_absolute_url(self) :
        return f'/store/{self.pk}/'
        
'''
class Check_table(models.Model) :
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    table_num = models.IntegerField(default=100)
    table_check = [models.BooleanField(default=False, blank=True, null=False) for x in range(100)]
'''

class Review(models.Model) :
    post = models.ForeignKey(Store, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def  __str__(self) :
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#review-{self.pk}'
    
    '''
    def get_avatar_url(self) :
        if self.author.socialaccount_set.exists() :
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            return f'https://doitdjango.com/avatar/id/998/dcdf2d00bddb8c6a/svg/{self.author.email}'
    '''