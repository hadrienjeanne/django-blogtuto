from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    '''home view'''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def about(request):
    '''about page view'''
    return render(request, "blog/about.html", {'title': 'About'})