from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Incredient(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, related_name='incredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
