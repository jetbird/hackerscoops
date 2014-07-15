from django.shortcuts import render_to_response
from article.models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def listing(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list,5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response('list.html', {'articles':articles})
