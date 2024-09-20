from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('user_edit/', views.user_edit, name='user_edit'),
    path('profile/<int:pk>/', views.DetailUserView.as_view(), name='profile'),
]
