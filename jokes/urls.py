from . import views
from django.urls import path

urlpatterns = [
    path('', views.jokes_page.as_view(), name='jokes_page'),
]