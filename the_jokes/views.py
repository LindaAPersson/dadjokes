from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Joke, Comment
from .forms import JokeForm, CommentForm

# Create your views here.

class joke_list(generic.ListView):

    queryset = Joke.objects.filter(status=1)
    template_name = "the_jokes/the_jokes.html"
    paginate_by = 1


def add_joke(request):
    last_joke = Joke.objects.order_by('-id').first()
    last_title_number = int(last_joke.title) if last_joke else 0
    next_title = last_title_number + 1 
    
    if request.method == "POST":
        joke_form = JokeForm(data=request.POST)
        
        if joke_form.is_valid():
            joke = joke_form.save(commit=False)
            joke.creator = request.user
            joke.title = next_title
            joke_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Joke submitted and awaiting approval'
            )

    joke_form = JokeForm()

    return render(
        request,
        "the_jokes/add_jokes.html",
        {
            "joke_form": joke_form,
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

def comment_edit(request, title, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Joke.objects.filter(status=1)
        joke = get_object_or_404(queryset, title=title)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.creator == request.user:
            comment = comment_form.save(commit=False)
            comment.joke_text = joke
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('jokes_detail', args=[title]))