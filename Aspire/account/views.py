from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from main.models import PostModel, Comment, Like
from main.views import r
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user = user)
            user_login = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user_login is not None:
                if user_login.is_active:
                    login(request, user_login)
                    return redirect('main:main_page')
                else:
                    return HttpResponse('Your account is disabled.')
            else:
                return HttpResponse('Invalid login or password.')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
            return redirect('main:main_page')
           
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'registration/user_edit.html', {'user_form': user_form, 'profile_form': profile_form})

class DetailUserView(DetailView):
    model = User
    template_name = 'registration/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        post_list = PostModel.objects.filter(author=user)
        for post in post_list:
            total_views = r.get(f'image:{post.id}:view')
            post.total_views = total_views.decode() if total_views else 0
            post.total_likes = post.likes.count

        context['profile'] = get_object_or_404(Profile, user=user)
        context['postmodel_list'] = post_list
        context['comments'] = Comment.objects.filter(post__in=post_list).count()
        context['likes'] = Like.objects.filter(post__in = post_list).count()

        return context


