from . import views
from django.urls import path

urlpatterns = [
    path('jokes/', views.JokeList.as_view(), name='jokes_page'),
    path('jokes/', views.showcomments, name='comments'),
    
]