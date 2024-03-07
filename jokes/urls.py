from . import views
from django.urls import path

urlpatterns = [
    path('', views.JokeList.as_view(), name='jokes_page'),
]