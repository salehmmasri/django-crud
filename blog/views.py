from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView,TemplateView, ListView, DetailView
from .models import Post
from django.urls import reverse_lazy, reverse

# # Create your views here.
class PostView(ListView):
    template_name = 'home.html'
    model=Post

class PostDetailsViewsp(DetailView):
    template_name = 'detail.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'blog_create.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'blog_update.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'blog_delete.html'
    model = Post
    success_url = reverse_lazy('home')

