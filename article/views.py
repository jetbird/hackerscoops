from django.shortcuts import render, render_to_response
from article.models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list,10)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render_to_response('home.html',
            {'articles':articles})


def article(request, slug):
    return render(request, 'article.html', {'article':Article.objects.get(slug=slug)})


def category(request, my_category):
    return render(request, 'category.html',
            {'my_category':Article.objects.filter(categories__name__startswith=my_category)[::-1]})


def login_view(request):
    pass
