from django import forms
from .models import PostModel
from django.forms import FileInput
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput)
    preview = forms.ImageField(widget=FileInput)
    class Meta:
        model = PostModel
        fields = ('title', 'image', 'preview')

    def clean_image(self):
        file = self.cleaned_data.get('image')
        valid_extensions = ['png', 'jpg', 'jpeg']
        ext = file.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise ValidationError('Insert a picture')

        return file

    def clean_preview(self):
        file = self.cleaned_data.get('preview')
        valid_extensions = ['png', 'jpg', 'jpeg']
        ext = file.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise ValidationError('Insert a picture')

        return file