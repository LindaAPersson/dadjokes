from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Joke(models.Model):
    title_number = models.CharField(max_length=100, unique=True)
    joke_text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joke_post")
    creator_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='jokes_like') 
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.title_number:  # If title is not provided by the user
            last_joke = Joke.objects.order_by('-id').first()  # Get the last joke
            if last_joke:
                last_joke_number = int(last_joke.title_number)
                self.title_number = str(last_joke_number + 1)  # Assign the next available number
            else:
                self.title_number = '1'  # If there are no jokes in the database yet, start with 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title_number} | written by {self.creator}"


class Comment(models.Model):
    joke_text = models.ForeignKey(Joke, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]