from . import views
from django.urls import path

urlpatterns = [
    path('the_jokes/', views.joke_list.as_view(), name='the_jokes_page'),
    
]