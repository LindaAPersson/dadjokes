from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Joke, Comment

# Create your views here.

class joke_list(generic.ListView):

    queryset = Joke.objects.filter(status=1)
    template_name = "the_jokes/the_jokes.html"
    paginate_by = 1


def joke_detail(request, title):
    queryset = Joke.objects.filter(status=1)
    jokes = get_object_or_404(queryset, title=title)

    return render(
        request,
        "the_jokes/jokes_detail.html",
        {"jokes": jokes},
    )