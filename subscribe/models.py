from django.db import models
from django.contrib.auth.models import User


class Subscribe(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return self.email


