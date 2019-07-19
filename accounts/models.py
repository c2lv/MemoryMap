from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

"""
유저정보
-id
로그인 정보 : username, password

"""


class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', '남성'),
        ('female', '여성'),
    )

    nickname = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=80, null=True, choices=GENDER_CHOICES)
    age = models.SmallIntegerField(null=True)
    # birth = models.

    country = CountryField()
    address = models.CharField(max_length=300, null=True)

