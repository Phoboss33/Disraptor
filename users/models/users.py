from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class User(AbstractUser):

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} {self.username}"
        else:
            return f"{self.username}"
