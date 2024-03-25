from .models import Comment, Joke, Category, Rating
from django import forms

# add jokes
class JokeForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image', 'category',)
        
    
# Edit jokes
class EditJokeForm(forms.ModelForm):
    
    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image',)    

# Like jokes
class LikesForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('likes',)

# comment jokes
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

# rate jokes
class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)

# age approved
class AgeForm(forms.ModelForm):

    class Meta:
        model = Joke
        fields = ('age_approved',)
        widgets = {'age_approved': forms.CheckboxInput(attrs={'class': 'filled-in show_all'})}

        
        




