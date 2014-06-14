from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Article(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.TextField()
    author = models.ForeignKey(User)
    body = models.TextField()
    categories = models.ManyToManyField(
        Category, related_name='articles', null=True)

    def __unicode__(self):
        return '%s by %s' %(self.title, self.author)


class Comment(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)
    article = models.ManyToManyField(Article, related_name='comments')
    content = models.TextField()

    def __unicode__(self):
        return self.content
