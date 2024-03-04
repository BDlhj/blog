from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
    )
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
