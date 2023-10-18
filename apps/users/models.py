from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from apps.users.managers import UserManager

from core.enums.regex_enum import RegEx
from core.models import BaseModel


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=[
        V.RegexValidator(*RegEx.NAME.value)
    ])
    surname = models.CharField(max_length=50, validators=[
        V.RegexValidator(*RegEx.NAME.value)
    ])
    age = models.IntegerField(validators=[
        V.MinValueValidator(16),
        V.MaxValueValidator(150)
    ])


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(*RegEx.PASSWORD.value)
    ])
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
