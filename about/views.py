from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

def contact_us(request):
    

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Message sent, you'll hear from us soon!")
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Error sending request!')

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form,
            
        },
    )