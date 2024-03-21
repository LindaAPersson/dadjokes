from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Joke(models.Model):

    title = models.CharField(max_length=200)
    joke_text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joke_creator")
    creator_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='joke_likes') 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    ratings = models.ManyToManyField(User, through='Rating', related_name='rated_jokes')


    class Meta:
        ordering = ["created_on"]
    
    def total_likes(self):
        return self.likes.count()
    
    def average_rating(self):
        return Rating.objects.filter(joke=self).aggregate(Avg('rating'))['rating__avg'] or 0

class Rating(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_creator")
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name="rating_joke")
    rating = models.IntegerField(default=0)


class Comment(models.Model):
    joke_text = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name="comments_text")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_creator")
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]