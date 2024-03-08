from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Joke, Comment

# Create your views here.

class JokeList(generic.ListView):
    queryset = Joke.objects.filter(status=1)
    template_name = "jokes/jokes.html"
    paginate_by = 1
    
def JokeLike(request, pk):
    post = get_object_or_404(JokeList, id=request.POST.get('like_buton'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('jokes_page', args=[str(pk)]))     

