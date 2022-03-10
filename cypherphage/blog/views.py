from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Cypher Phage',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 9, 2022'
    },
    {
        'author': 'Aditya Nain',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 10, 2022'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})