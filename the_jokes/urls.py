from . import views
from django.urls import path

urlpatterns = [
    path('the_jokes/', views.joke_list.as_view(), name='the_jokes_page'),
    path('the_jokes/<title>/', views.joke_detail, name='jokes_detail'),
    path('add_jokes/', views.add_joke, name='add_jokes')
    
]