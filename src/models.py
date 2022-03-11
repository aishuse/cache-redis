from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
