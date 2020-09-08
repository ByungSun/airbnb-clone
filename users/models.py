from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # Model Field를 찾아볼수 있다.
    bio = models.TextField(default="")
