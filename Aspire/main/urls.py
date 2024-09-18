from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('welcome/', views.welcome, name='welcome'),
  path('share_work/', views.add_post, name='add_post'),
  path('main/', views.ListPostView.as_view(), name='main_page'),
  path('edit_post/<slug:slug>/', views.EditPostView.as_view(), name='edit_post'),
  path('delete_post/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
]