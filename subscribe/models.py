from django.db import models
from django.contrib.auth.models import User

class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return self.email
