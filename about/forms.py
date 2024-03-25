from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    """
    A contact form the users can fill out to get in contact with the creators. 
    """ 
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', )
