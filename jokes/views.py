from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Joke, Comment

# Create your views here.

class JokeList(generic.ListView):

    queryset = Joke.objects.filter(status=1)
    template_name = "jokes/jokes.html"
    paginate_by = 1
    


def showcomments(request):
      
    queryset = Joke.objects.filter(status=1)
    post = get_object_or_404(queryset,)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "jokes/jokes.html",  
        {
            "joke": joke,
            "comments": comments,
            "comment_count": comment_count, 
        },
    )
    

