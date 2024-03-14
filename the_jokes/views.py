from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Joke, Comment
from .forms import JokeForm, CommentForm

# Create your views here.

class joke_list(generic.ListView):

    queryset = Joke.objects.filter(status=1)
    template_name = "the_jokes/the_jokes.html"
    paginate_by = 1


def add_joke(request):
    queryset = Joke.objects.all()

    if request.method == "POST":
        add_joke = JokeForm(data=request.POST)
        if add_joke.is_valid():
            comment = add_joke.save(commit=False)
            comment.creator = request.user
            
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Joke submitted and awaiting approval'
            )

    add_joke = JokeForm()

    return render(
        request,
        "the_jokes/add_jokes.html",
        {
            
            "add_joke": add_joke,
        },
    )



def joke_detail(request, title):
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)
    comments = joke.comments_text.all().order_by("-created_on")
    comment_count = joke.comments_text.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.creator = request.user
            comment.joke_text = joke
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "the_jokes/jokes_detail.html",
        {
            "joke": joke,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )