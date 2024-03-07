from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page.as_view, name='home_page'),
]