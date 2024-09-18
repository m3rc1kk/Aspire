from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView
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