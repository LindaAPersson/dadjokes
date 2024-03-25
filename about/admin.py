from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the contact model.
    """
    list_display = ['name'] 
