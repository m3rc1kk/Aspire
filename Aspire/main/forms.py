from django import forms
from .models import PostModel, Comment
from django.forms import FileInput
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput)
    preview = forms.ImageField(widget=FileInput)
    class Meta:
        model = PostModel
        fields = ('title', 'tags', 'image', 'preview')

    def clean_tags(self):
        file = self.cleaned_data.get('tags')
        for i in file:
            if len(i) > 10:
                raise ValidationError('Tag too big')

        if len(file) > 10:
            raise ValidationError('Too many tags (max 10)')

        return file

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)