from . import views
from django.urls import path

urlpatterns = [
    path('jokes/', views.joke_list, name='jokes_page'),
    path('jokes/', views.joke_detail, name='comments'),
    
]