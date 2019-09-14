from django.db import models

class Tag(models.Model):
    """Tags to be used in a recipe"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """Ingredients to be used in a recipe"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        