from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Joke(models.Model):

    title = models.CharField(max_length=200)
    joke_text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joke_creator")
    creator_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='joke_likes') 


    class Meta:
        ordering = ["?"]
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    joke_text = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name="comments_text")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_creator")
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]