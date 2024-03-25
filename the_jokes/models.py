from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Label(models.Model):
    """
    Model representing a label,
    that are used to filter the jokes.
    """
    label_name = models.CharField(max_length=100)

    def __str__(self):
        return self.label_name


class Category(models.Model):
    """
    Model representing categories,
    that are used to filter the jokes.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Joke(models.Model):
    """
    Model representing creating a joke.
    Returns the total number of likes for the joke,
    average rating for the joke and the formatted creation
    timestamp of the joke.
    """
    title = models.CharField(max_length=200)
    joke_text = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="joke_creator")
    creator_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='joke_likes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    ratings = models.ManyToManyField(
        User, through='Rating', related_name='rated_jokes')
    age_approved = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label, blank=True)

    class Meta:
        ordering = ["created_on"]

    def total_likes(self):
        return self.likes.count()

    def average_rating(self):
        return Rating.objects.filter(joke=self).aggregate(
            Avg('rating'))['rating__avg'] or 0

    def formatted_timestamp(self):
        return self.created_on.strftime("%Y-%m-%d")


class Rating(models.Model):
    """
    Model representing rating,
    that are used to give scores to the jokes.
    """
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rating_creator")
    joke = models.ForeignKey(
        Joke, on_delete=models.CASCADE, related_name="rating_joke")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Rating for {self.joke.title} by {self.creator}: {self.rating}"


class Comment(models.Model):
    """
    Model representing commments,
    that are used to inteact and comment on the jokes.
    """
    joke_text = models.ForeignKey(
        Joke, on_delete=models.CASCADE, related_name="comments_text")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_creator")
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.creator} on {self.joke_text.title}"
