from django.shortcuts import render
from django.views import generic
from .models import Joke

# Create your views here.

class JokeList(generic.ListView):
    queryset = Joke.objects.filter(status=1)
    template_name = "jokes/jokes.html"
    