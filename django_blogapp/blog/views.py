from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def home(request):
    '''home view'''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # by default: <app>/<model>_<viewtype>.html -> blog/post_list.html
    context_object_name = 'posts'

def about(request):
    '''about page view'''
    return render(request, "blog/about.html", {'title': 'About'})