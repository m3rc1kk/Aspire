from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # Путь будет что-то вроде: 'profile_pictures/<username>/<filename>'
    return f'profile_pictures/{instance.user.username}/{filename}'

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  avatar = models.ImageField(null=True, blank=True, upload_to = user_directory_path)

  def __str__(self):
    return f'{self.user.username}'