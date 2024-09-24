from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager

def generate_unique_slug(instance):
    original_slug = slugify(instance.title)
    unique_slug = original_slug
    counter = 1

    while PostModel.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{original_slug}-{counter}"
        counter += 1

    return unique_slug

def image_directory_path(instance, filename):
    return f'{instance.author.username}/posts/image/{filename}'

def preview_directory_path(instance, filename):
    return f'{instance.author.username}/posts/preview/{filename}'

class PostModel(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to= image_directory_path)
    preview = models.ImageField(upload_to= preview_directory_path, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if self.pk:
            old_title = PostModel.objects.get(pk=self.pk).title
            if old_title != self.title:
                self.slug = generate_unique_slug(self.title)
        else:
            self.slug = generate_unique_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Posts'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:detail_post', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-created']
        db_table = 'Comments'
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Comment from {self.author}'