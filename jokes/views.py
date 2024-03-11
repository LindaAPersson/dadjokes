from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Joke, Comment

# Create your views here.

class JokeList(generic.ListView):
    queryset = Joke.objects.filter(status=1)
    template_name = "jokes/jokes.html"
    paginate_by = 1
    
def CommentsView(request, id):
    queryset = Joke.objects.filter(status=1)
    show = get_object_or_404(queryset, id=id)
    comments = show.comments.all().order_by("-created_on")
    comment_count = show.comments.filter(approved=True).count()

    return render(
        request,
        "jokes/jokes.html",
        {
            "comments": comments,
            "comment_count": comment_count, 
        },
    )
  

