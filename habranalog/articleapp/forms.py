from articleapp.models import Article, ArticlesBlock
from django.forms import ModelForm, Select,ModelChoiceField
from django import forms
from django.contrib.auth.models import User


class CreateArticleForm(ModelForm):
    class Meta:
        model=Article
        fields=['title','prememo','image']

class CreateBlocksForm(ModelForm):
    article = forms.ModelChoiceField(queryset=Article.objects.all(),widget=Select(attrs={'class': 'form-control'}))
    class Meta:
        model = ArticlesBlock
        fields = ['title', 'memo', 'image', 'article']


class ChangeBlockForm(forms.ModelForm):
    class Meta:
        model = ArticlesBlock
        fields = ['title', 'memo']

class ChangeUserName(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

