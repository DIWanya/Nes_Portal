from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory']
        labels = {'author': 'Автор', 'title': 'Заголовок', 'text': 'Текст новости', 'postCategory': 'Категория'}
