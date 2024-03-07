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

    def save(self, *args, **kwargs):
        if not self.title_number: 
            last_joke = Joke.objects.order_by('-id').first()  # Get the last joke
            if last_joke:
                last_joke_number = int(last_joke.title_number)
                self.title = str(last_joke_number + 1)  # Assign the next available number
            else:
                self.title_number = '1'  # If there are no jokes in the database yet, start with 1
        super().save(*args, **kwargs)