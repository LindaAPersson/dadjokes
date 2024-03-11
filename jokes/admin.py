from django.contrib import admin
from .models import Joke, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Joke)
class JokeAdmin(SummernoteModelAdmin):

    list_display = ('id', 'creator', 'status')
    search_fields = ['id']
    list_filter = ('creator', 'status')
    summernote_fields = ('joke_text',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ['id','creator']
    search_fields = ['id']
    list_filter = ('creator', 'approved')
    summernote_fields = ('joke_text',)