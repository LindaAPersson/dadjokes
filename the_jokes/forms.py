from .models import Comment, Joke, Category, Rating
from django import forms


class JokeForm(forms.ModelForm):
    """
    A form for adding jokes
    """
    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image', 'category',)
        
    
class EditJokeForm(forms.ModelForm):
    """
    A form for edit jokes
    """ 
    class Meta:
        model = Joke
        fields = ('joke_text', 'creator_image',)    


class LikesForm(forms.ModelForm):
    """
    A form for like jokes
    """ 

    class Meta:
        model = Joke
        fields = ('likes',)


class CommentForm(forms.ModelForm):
    """
    A form for comment on jokes
    """ 
    class Meta:
        model = Comment
        fields = ('comment_text',)


class RateForm(forms.ModelForm):
    """
    A form for rating jokes
    """ 
    class Meta:
        model = Rating
        fields = ('rating',)


class AgeForm(forms.ModelForm):
    """
    A form for age approvel. The users can filter the jokes
    depending on age approved. 
    """
    class Meta:
        model = Joke
        fields = ('age_approved',)
        widgets = {'age_approved': forms.CheckboxInput(attrs={'class': 'filled-in show_all'})}

        
        




