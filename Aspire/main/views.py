from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from taggit.models import Tag
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .models import PostModel, Comment
from django.views.decorators.http import require_POST
import redis
from django.conf import settings

r = redis.Redis(host = settings.REDIS_HOST, port = settings.REDIS_PORT, db = settings.REDIS_DB)

def welcome(request):
  return render(request, 'main/welcome.html')


def add_post(request):
  if request.method == 'POST':
    post = PostForm(request.POST, request.FILES)
    if post.is_valid():
      post_form = post.save(commit=False)
      post_form.author = request.user
      post_form.save()
      original_slug = slugify(post_form.title)
      slug = original_slug
      counter = 1

      while PostModel.objects.filter(slug=slug).exists():
          slug = f"{original_slug}-{counter}"
          counter += 1

      post_form.slug = slug
      post_form.save()
      post.save_m2m()
      return redirect('main:main_page')
  else:
    post = PostForm()

  return render(request, 'main/add_post.html', {'form': post})


class ListPostView(ListView):
  model = PostModel
  template_name = 'main/main_page.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    posts = self.object_list

    for post in posts:
      total_views = r.get(f'image:{post.id}:view')
      post.total_views = total_views.decode() if total_views else 0

    context['posts'] = posts
    return context

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['comments'] = self.object.comments.all()
    context['form'] = CommentForm()
    context['total_views'] = r.incr(f'image:{self.object.id}:view')
    return context



def post_list_tag(request, tag_slug = None):
  tag = get_object_or_404(Tag, slug=tag_slug)
  post_list = PostModel.objects.filter(tags__in=[tag])

  return render(request, 'main/tag_page.html', {'post_list': post_list, 'tag':tag})


@require_POST
def post_comment(request, post_slug):
  post = get_object_or_404(PostModel, slug = post_slug)
  form = CommentForm(request.POST)
  if form.is_valid():
    comment = form.save(commit=False)
    comment.post = post
    comment.author = request.user
    comment.save()
  return render(request, 'main/comment.html', {'form': form, 'post': post})


class DeleteCommentView(DeleteView):
  model = Comment
  template_name = 'main/delete_comment.html'
  def get_success_url(self):
    post_slug = self.object.post.slug
    return reverse_lazy('main:detail_post', args=[post_slug])