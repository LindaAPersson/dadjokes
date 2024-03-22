from .models import Comment, Joke, Category, Rating
from django import forms

class JokeForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image', 'category', 'age_approved')
        widgets = {'age_approved': forms.CheckboxInput(attrs={'class': 'filled-in'})}
    

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

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)






