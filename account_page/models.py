from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
#AbstractBaseUser을 상속받아 생성

class UserManager(BaseUserManager):
    def create_user(self, nickname, email, date_of_birth, is_seller, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            date_of_birth=date_of_birth,
            is_seller=is_seller,
        )
        #email, date_of_birth, is_active, is_admin 4개의 필드를 가짐

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, date_of_birth, is_seller, password):
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
            date_of_birth=date_of_birth,
            is_seller=is_seller,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(default='', max_length=10, null=False, blank=False, unique=True)
    date_of_birth = models.DateField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'date_of_birth', 'is_seller']

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    #커스텀 유저 모델을 기본 유저 모델로 사용하기 위해 구현
    @property
    def is_staff(self):
        return self.is_admin