from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('welcome/', views.welcome, name='welcome'),
  path('share_work/', views.add_post, name='add_post'),
  path('main/', views.ListPostView.as_view(), name='main_page'),
  path('edit_post/<slug:slug>/', views.EditPostView.as_view(), name='edit_post'),
  path('delete_post/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
  path('detail_post/<slug:slug>/', views.DetailPostView.as_view(), name='detail_post'),
  path('main-tag/<slug:tag_slug>/', views.post_list_tag, name='post_list_tag'),
  path('<slug:post_slug>/comment/', views.post_comment, name='post_comment'),

  path('delete_comment/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
  path('like/<slug:post_slug>/', views.PostLike, name='like_post'),
]