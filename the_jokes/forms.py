from .models import Comment, Joke
from django import forms

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ('title', 'joke_text', 'creator', 'creator_image', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)