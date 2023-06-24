from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):

        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Must have is_staff value set to True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Must have is_superuser set to True")

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username
