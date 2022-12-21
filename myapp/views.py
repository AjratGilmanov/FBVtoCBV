from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # здесь передаем переменную с именем name_variable
        # и ее значением value_variable
        context['title'] = BlogDetailView
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
 
 
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body', 'img']
 
 
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body','img']
 
 
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')