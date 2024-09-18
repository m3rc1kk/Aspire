from django import forms
from .models import PostModel
from django.forms import FileInput

class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput)
    preview = forms.ImageField(widget=FileInput)
    class Meta:
        model = PostModel
        fields = ('title', 'image', 'preview')