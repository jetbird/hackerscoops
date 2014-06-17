from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.


def home(request):
    return render(request, 'home.html', {'articles':Article.objects.all()[:10]})


def article(request, slug):
    return render(request, 'article.html', {'article':Article.objects.get(slug=slug)})
