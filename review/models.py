from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    review = models.TextField()

    def __str__(self):
        return self.name
