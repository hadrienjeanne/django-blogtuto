from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def home(request):
    '''home view'''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # by default <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # template by default blog/post_detail.html
    model = Post

class PostCreateView(CreateView):
    # template by default blog/post_form.html
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
 


def about(request):
    '''about page view'''
    return render(request, "blog/about.html", {'title': 'About'})
