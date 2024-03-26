from django.contrib import admin
from .models import Joke, Comment, Category, Rating, Label

# Register your models here.


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Joke model.
    """
    list_display = ('title', 'creator', 'status', 'category')
    search_fields = ['title']
    list_filter = ('creator', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Comment model.
    """
    list_display = ['id', 'creator']
    search_fields = ['id']
    list_filter = ('creator', 'approved')


@admin.register(Category)
class Category(admin.ModelAdmin):
    """
    Admin configuration for Category model.
    """
    list_display = ['name', 'id']
    summernote_fields = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Rating model.
    """
    list_display = ['creator', 'joke']


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    """
    Admin configuration for Label model.
    """
    list_display = ['label_name']
