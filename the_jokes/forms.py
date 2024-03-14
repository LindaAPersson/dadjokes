from .models import Comment, Joke
from django import forms

class JokeForm(forms.ModelForm):
    title = forms.CharField(initial = Joke.id)
    class Meta:
        model = Joke
        fields = ('title', 'joke_text', 'creator_image', )

       

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)