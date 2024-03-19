from .models import Comment, Joke, Category
from django import forms

class JokeForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image', 'category', )
    

class EditJokeForm(forms.ModelForm):
    
    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image',)     

class LikesForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('likes',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)






