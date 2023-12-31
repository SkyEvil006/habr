from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



class Article(models.Model):
    title = models.CharField(max_length=150)
    prememo = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articleapp/images', null=True, blank=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    class Meta:
        permissions =[('can_read_article', 'can read article')]

    def __str__(self):
        return str(self.id) + '__' + self.title


class ArticlesBlock(models.Model):
    title = models.CharField(max_length=150)
    memo = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='articleapp/images', null=True, blank=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + '__' + self.title


class Views(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    class Meta:
        unique_together=('user', 'article',)



class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
