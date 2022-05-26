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

class Check_table(models.Model) :
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    table_num = models.IntegerField(default=100)
    table_check_001 = models.BooleanField(default=False, blank=True, null=False)
    table_check_002 = models.BooleanField(default=False, blank=True, null=False)
    table_check_003 = models.BooleanField(default=False, blank=True, null=False)
    table_check_004 = models.BooleanField(default=False, blank=True, null=False)
    table_check_005 = models.BooleanField(default=False, blank=True, null=False)
    table_check_006 = models.BooleanField(default=False, blank=True, null=False)
    table_check_007 = models.BooleanField(default=False, blank=True, null=False)
    table_check_008 = models.BooleanField(default=False, blank=True, null=False)
    table_check_009 = models.BooleanField(default=False, blank=True, null=False)
    table_check_010 = models.BooleanField(default=False, blank=True, null=False)
    table_check_011 = models.BooleanField(default=False, blank=True, null=False)
    table_check_012 = models.BooleanField(default=False, blank=True, null=False)
    table_check_013 = models.BooleanField(default=False, blank=True, null=False)
    table_check_014 = models.BooleanField(default=False, blank=True, null=False)
    table_check_015 = models.BooleanField(default=False, blank=True, null=False)
    table_check_016 = models.BooleanField(default=False, blank=True, null=False)
    table_check_017 = models.BooleanField(default=False, blank=True, null=False)
    table_check_018 = models.BooleanField(default=False, blank=True, null=False)
    table_check_019 = models.BooleanField(default=False, blank=True, null=False)
    table_check_020 = models.BooleanField(default=False, blank=True, null=False)
    table_check_021 = models.BooleanField(default=False, blank=True, null=False)
    table_check_022 = models.BooleanField(default=False, blank=True, null=False)
    table_check_023 = models.BooleanField(default=False, blank=True, null=False)
    table_check_024 = models.BooleanField(default=False, blank=True, null=False)
    table_check_025 = models.BooleanField(default=False, blank=True, null=False)
    table_check_026 = models.BooleanField(default=False, blank=True, null=False)
    table_check_027 = models.BooleanField(default=False, blank=True, null=False)
    table_check_028 = models.BooleanField(default=False, blank=True, null=False)
    table_check_029 = models.BooleanField(default=False, blank=True, null=False)
    table_check_030 = models.BooleanField(default=False, blank=True, null=False)
    table_check_031 = models.BooleanField(default=False, blank=True, null=False)
    table_check_032 = models.BooleanField(default=False, blank=True, null=False)
    table_check_033 = models.BooleanField(default=False, blank=True, null=False)
    table_check_034 = models.BooleanField(default=False, blank=True, null=False)
    table_check_035 = models.BooleanField(default=False, blank=True, null=False)
    table_check_036 = models.BooleanField(default=False, blank=True, null=False)
    table_check_037 = models.BooleanField(default=False, blank=True, null=False)
    table_check_038 = models.BooleanField(default=False, blank=True, null=False)
    table_check_039 = models.BooleanField(default=False, blank=True, null=False)
    table_check_040 = models.BooleanField(default=False, blank=True, null=False)
    table_check_041 = models.BooleanField(default=False, blank=True, null=False)
    table_check_042 = models.BooleanField(default=False, blank=True, null=False)
    table_check_043 = models.BooleanField(default=False, blank=True, null=False)
    table_check_044 = models.BooleanField(default=False, blank=True, null=False)
    table_check_045 = models.BooleanField(default=False, blank=True, null=False)
    table_check_046 = models.BooleanField(default=False, blank=True, null=False)
    table_check_047 = models.BooleanField(default=False, blank=True, null=False)
    table_check_048 = models.BooleanField(default=False, blank=True, null=False)
    table_check_049 = models.BooleanField(default=False, blank=True, null=False)
    table_check_050 = models.BooleanField(default=False, blank=True, null=False)
    table_check_051 = models.BooleanField(default=False, blank=True, null=False)
    table_check_052 = models.BooleanField(default=False, blank=True, null=False)
    table_check_053 = models.BooleanField(default=False, blank=True, null=False)
    table_check_054 = models.BooleanField(default=False, blank=True, null=False)
    table_check_055 = models.BooleanField(default=False, blank=True, null=False)
    table_check_056 = models.BooleanField(default=False, blank=True, null=False)
    table_check_057 = models.BooleanField(default=False, blank=True, null=False)
    table_check_058 = models.BooleanField(default=False, blank=True, null=False)
    table_check_059 = models.BooleanField(default=False, blank=True, null=False)
    table_check_060 = models.BooleanField(default=False, blank=True, null=False)
    table_check_061 = models.BooleanField(default=False, blank=True, null=False)
    table_check_062 = models.BooleanField(default=False, blank=True, null=False)
    table_check_063 = models.BooleanField(default=False, blank=True, null=False)
    table_check_064 = models.BooleanField(default=False, blank=True, null=False)
    table_check_065 = models.BooleanField(default=False, blank=True, null=False)
    table_check_066 = models.BooleanField(default=False, blank=True, null=False)
    table_check_067 = models.BooleanField(default=False, blank=True, null=False)
    table_check_068 = models.BooleanField(default=False, blank=True, null=False)
    table_check_069 = models.BooleanField(default=False, blank=True, null=False)
    table_check_070 = models.BooleanField(default=False, blank=True, null=False)
    table_check_071 = models.BooleanField(default=False, blank=True, null=False)
    table_check_072 = models.BooleanField(default=False, blank=True, null=False)
    table_check_073 = models.BooleanField(default=False, blank=True, null=False)
    table_check_074 = models.BooleanField(default=False, blank=True, null=False)
    table_check_075 = models.BooleanField(default=False, blank=True, null=False)
    table_check_076 = models.BooleanField(default=False, blank=True, null=False)
    table_check_077 = models.BooleanField(default=False, blank=True, null=False)
    table_check_078 = models.BooleanField(default=False, blank=True, null=False)
    table_check_079 = models.BooleanField(default=False, blank=True, null=False)
    table_check_080 = models.BooleanField(default=False, blank=True, null=False)
    table_check_081 = models.BooleanField(default=False, blank=True, null=False)
    table_check_082 = models.BooleanField(default=False, blank=True, null=False)
    table_check_083 = models.BooleanField(default=False, blank=True, null=False)
    table_check_084 = models.BooleanField(default=False, blank=True, null=False)
    table_check_085 = models.BooleanField(default=False, blank=True, null=False)
    table_check_086 = models.BooleanField(default=False, blank=True, null=False)
    table_check_087 = models.BooleanField(default=False, blank=True, null=False)
    table_check_088 = models.BooleanField(default=False, blank=True, null=False)
    table_check_089 = models.BooleanField(default=False, blank=True, null=False)
    table_check_090 = models.BooleanField(default=False, blank=True, null=False)
    table_check_091 = models.BooleanField(default=False, blank=True, null=False)
    table_check_092 = models.BooleanField(default=False, blank=True, null=False)
    table_check_093 = models.BooleanField(default=False, blank=True, null=False)
    table_check_094 = models.BooleanField(default=False, blank=True, null=False)
    table_check_095 = models.BooleanField(default=False, blank=True, null=False)
    table_check_096 = models.BooleanField(default=False, blank=True, null=False)
    table_check_097 = models.BooleanField(default=False, blank=True, null=False)
    table_check_098 = models.BooleanField(default=False, blank=True, null=False)
    table_check_099 = models.BooleanField(default=False, blank=True, null=False)
    table_check_100 = models.BooleanField(default=False, blank=True, null=False)


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