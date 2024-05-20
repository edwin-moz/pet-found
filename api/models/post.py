from django.db import models

class Post(models.Model):
    contact_email = models.EmailField()
    date_added = models.DateTimeField()
    pet_behavior = models.ForeignKey("PetBehavior", on_delete=models.CASCADE, related_name="pet_behavior_posts")
    pet_age = models.IntegerField()
    pet_breed = models.CharField(max_length=100)
    pet_color = models.CharField(max_length=100)
    pet_description = models.TextField()
    pet_favorite_snack = models.CharField(max_length=100)
    pet_image_url = models.URLField()
    pet_name = models.CharField(max_length=100)