from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='home'),
    
]
 #TemplateView.as_view(template_name='home/index.html')