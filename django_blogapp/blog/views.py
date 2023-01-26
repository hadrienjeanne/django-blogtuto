from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    '''home view function'''
    return HttpResponse('<h1>Blog Home</h1>')
