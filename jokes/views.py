from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Joke, Comment

# Create your views here.

def joke_list(request):

    jokes = Joke.objects.filter(status=1)
    return render(
        request, 
        'jokes/jokes.html', 
        {'jokes': jokes}
        )
    


def joke_detail(request, joke_id):
      
    queryset = Joke.objects.filter(status=1)
    post = get_object_or_404(queryset, joke_id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "jokes/jokes.html",  
        {
            'joke': joke,
            "comments": comments,
            "comment_count": comment_count, 
        },
    )
    

