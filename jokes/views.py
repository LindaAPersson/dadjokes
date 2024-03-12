from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Joke, Comment

# Create your views here.

class joke_list(generic.ListView):

    queryset = Joke.objects.filter(status=1)
    template_name = "jokes/jokes.html"
    paginate_by = 1
    


def joke_detail(request, joke_id):
    
    joke = get_object_or_404(Joke, id=joke_id)
    comments = Comment.objects.filter(joke_text=joke, approved=True).order_by("-created_on")
    comment_count = joke.comments.filter(approved=True).count()

    return render(
        request,
        "jokes/jokes.html",  
        {
            "joke": joke,
            "comments": comments,
            "comment_count": comment_count, 
        },
    )
    

