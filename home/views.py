from django.shortcuts import render

def index(request):
    """
    Returns the index.html file
    """
    return render(request, 'home/index.html')