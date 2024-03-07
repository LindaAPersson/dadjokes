from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Joke(models.Model):
    title_number = models.CharField(max_length=100, unique=True)
    joke_text = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="joke_post")
    creator_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='jokes_like') 
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)