from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager


# Create your models here.

def upload_path(file, model)->str:
    return f'avatars/{model.pk}/{file}'


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to=upload_path)

    objects = UserManager()

    USERNAME_FIELD = None
    REQUIRED_FIELDS = ["email"]
