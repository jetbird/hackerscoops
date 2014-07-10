from django.shortcuts import render
from article.models import Article

def home(request):
    return render(request, 'home.html',
            {'articles':Article.objects.all()[::-1][:10]})


def article(request, slug):
    return render(request, 'article.html', {'article':Article.objects.get(slug=slug)})


def category(request, my_category):
    return render(request, 'category.html',
            {'my_category':Article.objects.filter(categories__name__startswith=my_category)[::-1]})


def login_view(request):
    pass
