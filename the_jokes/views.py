from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Joke, Comment, Category, Rating, Label
from .forms import JokeForm, CommentForm, EditJokeForm, LikesForm, RateForm, AgeForm

# Create your views here.


def JokeList(request):
    """
    This function retrieves all the jokes, age form, age badges,
    labels, average rating/score, and categories from the database.
    It then renders this information to the 'the_jokes.html' template.
    Additionally, the function handles pagination.
    """
    queryset = Joke.objects.filter(status=1)
    categories = Category.objects.all()
    age_form = AgeForm(request.GET or None)
    labels = Label.objects.all()
    age_approved = queryset.filter(age_approved=True)

    if age_form.is_valid():
        age_approved = age_form.cleaned_data.get('age_approved')

        if age_approved:
            queryset = queryset.filter(age_approved=True)

    selected_labels = request.GET.getlist('label_name')
    if selected_labels:
        queryset = queryset.filter(labels__label_name__in=selected_labels)

    if age_approved and selected_labels:
        queryset = queryset.filter(
            age_approved=True, labels__label_name__in=selected_labels)

    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    for joke in queryset:
        joke.average_rating = joke.average_rating()

    return render(request, "the_jokes/the_jokes.html", {
        'queryset': queryset,
        'categories': categories,
        'age_form': age_form,
        'labels': labels
    })


def rate(request, title):
    """
    This function allows users to rate jokes. it retrieves the rating value
    submitted by the user and saves it for the specified joke.
    If the rating already exists for the user
    and joke combination, it updates the existing rating.
    """
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)

    if request.method == 'POST':
        joke = get_object_or_404(queryset, title=title)
        rating_value = int(request.POST.get('rating'))
        rating, created = Rating.objects.get_or_create(
            creator=request.user, joke=joke)
        rating.rating = rating_value
        rating.save()
        return HttpResponseRedirect(reverse('the_jokes_page'))
    else:
        messages.add_message(request, messages.ERROR, 'Error adding rating!')
        return HttpResponseRedirect(reverse('the_jokes_page'))


def category(request, name):
    """
    This function retrieves jokes belonging to the specified
    category from the database. If the form is valid and age approval
    is provided, it filters the jokes accordingly.
    Additionally, the function handles pagination.
    """
    categories = Category.objects.all()
    age_form = AgeForm(request.GET or None)

    if age_form.is_valid():
        age_approved = age_form.cleaned_data.get('age_approved')
        category = Category.objects.get(name=name)
        jokes = Joke.objects.filter(status=1, category=category)
        if age_approved:
            jokes = jokes.filter(age_approved=True)
    else:
        category = Category.objects.get(name=name)
        jokes = Joke.objects.filter(status=1, category=category)

    paginator = Paginator(jokes, 10)
    page_number = request.GET.get('page')
    try:
        jokes = paginator.page(page_number)
    except PageNotAnInteger:
        jokes = paginator.page(1)
    except EmptyPage:
        jokes = paginator.page(paginator.num_pages)

    try:
        category = Category.objects.get(name=name)
        categories = Category.objects.all()
        return render(
            request,
            'the_jokes/category.html',
            {
                'jokes': jokes,
                'category': category,
                'categories': categories,
                'age_form': age_form
            })
    except Category.DoesNotExist:
        messages.add_message(
                request, messages.SUCCESS,
                "That category doesn't exist"
            )
        return redirect('the_jokes_page')


def add_joke(request):
    """
    This function retrieves the last added joke from the
    database to generate the next title number.
    It retrieves all available categories from the database.
    If the form is valid, it saves the joke with the next
    title number and the current user as the creator.
    """
    last_joke = Joke.objects.order_by('-id').first()
    last_title_number = int(last_joke.title) if last_joke else 0
    next_title = last_title_number + 1
    category = Category.objects.all()

    if request.method == "POST":
        joke_form = JokeForm(request.POST, request.FILES)

        if joke_form.is_valid():
            joke = joke_form.save(commit=False)
            joke.creator = request.user
            joke.title = next_title
            joke_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Joke commited but waiting on approval!')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Error adding joke!')
    joke_form = JokeForm()

    return render(
        request,
        "the_jokes/add_jokes.html",
        {
            "joke_form": joke_form,
            "category": category
        },
    )


def joke_edit(request, title):
    """
    This function retrieves the joke to be edited from the database.
    If the form is valid, it updates the joke details.
    """
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)
    edit_joke_form = EditJokeForm(instance=joke)

    if request.method == "POST":
        edit_joke_form = EditJokeForm(
             request.FILES, data=request.POST, instance=joke)

        if edit_joke_form.is_valid() and joke.creator == request.user:
            joke.creator_id = request.user.id
            joke = edit_joke_form.save(commit=False)
            joke.status = 0
            joke.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Joke Updated but waiting on approval!')
            return redirect('home')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating joke!')
    return render(
        request,
        "the_jokes/edit_jokes.html", {
            "joke": joke,
            "edit_joke_form": edit_joke_form,
            })


def joke_delete(request, title, joke_id):
    """
    This function delets jokes.
    If the request user is the creator of the joke,
    a success message will be displayed. Otherwise, an error message will
    be displayed indicating that only the creator can delete the joke.
    """
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)

    if joke.creator == request.user:
        joke.delete()
        messages.add_message(request, messages.SUCCESS, 'Joke deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own jokes!')

    return HttpResponseRedirect(reverse('the_jokes_page'))


def joke_detail(request, title):
    """
    This function retrieves the joke and comments associated
    with the joke and orders them by creation date.
    It gets the total number of approved comments.
    Retrieves the likes for the joke and calculates the total number of likes.
    """
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)
    comments = joke.comments_text.all().order_by("-created_on")
    comment_count = joke.comments_text.filter(approved=True).count()
    likes = get_object_or_404(Joke, title=title)
    total_likes = likes.total_likes()
    likes_count = total_likes

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
        else:
            messages.add_message(
                request, messages.ERROR, 'Error creating comment!')

    comment_form = CommentForm()

    liked = False
    if likes.likes.filter(id=request.user.id).exists():
        liked = True

    return render(
        request,
        "the_jokes/jokes_detail.html",
        {
            "joke": joke,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "likes_count": likes_count,
            "liked": liked,
        },
    )


def like_joke(request, title, joke_id):
    """
    This function checks if the current user has already liked the joke.
    If the user has already liked the joke, removes the like;
    otherwise, adds the like.
    """
    joke = get_object_or_404(Joke, title=title)
    liked = False

    if joke.likes.filter(id=request.user.id).exists():
        joke.likes.remove(request.user)
        liked = False
    else:
        joke.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('jokes_detail', args=[title]))


def comment_edit(request, title, comment_id):
    """
    This function retrieves the joke and its comments.
    If the form is valid and the comment belongs to
    the current user, updates the comment text.
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
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')
    return HttpResponseRedirect(reverse('jokes_detail', args=[title]))


def comment_delete(request, title, comment_id):
    """
    This fuction deletes the comments,
    and displays a success or error message.
    """
    queryset = Joke.objects.filter(status=1)
    joke = get_object_or_404(queryset, title=title)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.creator == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
             request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('jokes_detail', args=[title]))


def custom_404_view(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Custom handler for 500 (Server Error) errors.
    """
    return render(request, '500.html', status=500)
