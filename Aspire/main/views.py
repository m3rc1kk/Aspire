from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from account.models import Profile
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .models import PostModel
def welcome(request):
  return render(request, 'main/welcome.html')


def add_post(request):
  if request.method == 'POST':
    post = PostForm(request.POST, request.FILES)
    if post.is_valid():
      post_form = post.save(commit=False)
      post_form.author = request.user
      post_form.save()
      return redirect('main:main_page')
  else:
    post = PostForm()

  return render(request, 'main/add_post.html', {'form': post})


class ListPostView(ListView):
  model = PostModel
  template_name = 'main/main_page.html'

class DeletePostView(DeleteView):
  model = PostModel
  template_name = 'main/delete_post.html'
  slug_field = 'slug'
  success_url = reverse_lazy('main:main_page')

class EditPostView(UpdateView):
  model = PostModel
  form_class = PostForm
  slug_field = 'slug'
  template_name = 'main/add_post.html'
  success_url = reverse_lazy('main:main_page')

class DetailPostView(DetailView):
  model = PostModel
  context_object_name = 'post'
  template_name = 'main/post_detail.html'
  slug_field = 'slug'


