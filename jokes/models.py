from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Joke(models.Model):
    
    
    joke_text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joke_post")
    creator_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='jokes_like') 
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ["?"]

    
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    joke_text = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.comment_text} by {self.creator}"