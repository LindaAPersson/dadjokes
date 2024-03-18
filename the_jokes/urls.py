from . import views
from django.urls import path

urlpatterns = [
    path('the_jokes/', views.joke_list.as_view(), name='the_jokes_page'),
    path('the_jokes/<title>/', views.joke_detail, name='jokes_detail'),
    path('add_jokes/', views.add_joke, name='add_jokes'),
    path('the_jokes/<title>/edit_joke/', views.joke_edit, name='joke_edit'),
    path('the_jokes/<title>/edit_joke/delete_joke/<int:joke_id>', views.joke_delete, name='joke_delete'),
    path('the_jokes/<title>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('the_jokes/<title>/delete_comment/<int:comment_id>', views.comment_delete, name='delete_comment'),
    path('the_jokes/<title>/<int:joke_id>', views.like_joke, name='like_jokes'),
    path('the_jokes/category/<str:name>', views.category, name='category'),
    
    
]