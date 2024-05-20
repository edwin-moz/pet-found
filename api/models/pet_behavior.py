from django.db import models

class PetBehavior(models.Model):
    behavior = models.CharField(max_length=100)