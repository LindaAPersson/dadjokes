from django.shortcuts import render
from django.views import generic
from .models import Joke

# Create your views here.

class JokeList(generic.ListView):
    model = Joke
    template_name = "jokes/jokes.html"
    
    