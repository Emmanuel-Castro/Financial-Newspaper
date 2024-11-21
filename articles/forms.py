#from django import forms
from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'author', 'date', 'content']

        def save(self):
            Article.objects.create(
                title = self.cleaned_data['title'],
                subtitle = self.cleaned_data['subtitle'],
                author = self.cleaned_data['author'],
                date = self.cleaned_data['date'],
                content = self.cleaned_data['content'],
        )        