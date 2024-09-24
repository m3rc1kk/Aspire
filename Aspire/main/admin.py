from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
  pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id']