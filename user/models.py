from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from pages.models import BaseModel
from user.manager import CustomUserManager


class UserModel(AbstractUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, unique=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
