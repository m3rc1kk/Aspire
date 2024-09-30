from audioop import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    return f'{instance.user.username}/profile_avatars/{filename}'

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  avatar = models.ImageField(null=True, blank=True, upload_to = user_directory_path)

  def __str__(self):
    return f'{self.user.username}'




