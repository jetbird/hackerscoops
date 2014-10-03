from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import markdown

# Create your models here.

def markdown_to_html(markdownText):
    html = markdown.markdown(markdownText)

    return html

class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    imagename = models.TextField()
    articleimage = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __unicode__(self):
        return "%s is %s" %(self.imagename, self.articleimage)


class Article(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=130)
    title = models.TextField()
    photo = models.ManyToManyField(
            Photo, related_name='photos')
    author = models.ForeignKey(User)
    body = models.TextField()
    categories = models.ManyToManyField(
        Category, related_name='articles', null=True)

    def __unicode__(self):
        return '%s by %s' %(self.title, self.author)

    def body_html(self):
        return markdown_to_html(self.body)


class Comment(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)
    article = models.ManyToManyField(Article, related_name='comments')
    content = models.TextField()

    def __unicode__(self):
        return self.content
