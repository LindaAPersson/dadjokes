from django.contrib import admin
from .models import Joke, Comment, Category, Rating, Label
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Joke)
class JokeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'creator', 'status', 'category')
    search_fields = ['title']
    list_filter = ('creator', 'status')
    summernote_fields = ('joke_text',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ['id', 'creator']
    search_fields = ['id']
    list_filter = ('creator', 'approved')
    summernote_fields = ('comment_text',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'id']
    summernote_fields = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['creator', 'joke']


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['label_name']
