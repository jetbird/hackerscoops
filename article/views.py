from django.shortcuts import render
from article.models import Article


def home(request):
    return render(request, 'home.html', {'articles':Article.objects.all()[:10][::-1]})


def article(request, slug):
    return render(request, 'article.html', {'article':Article.objects.get(slug=slug)})
