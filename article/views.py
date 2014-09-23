from django.shortcuts import render, HttpResponse
from article.models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from article.forms import CommentForm


def home(request):
    article_list = Article.objects.all()[::-1]
    paginator = Paginator(article_list,10)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request,'home.html',
            {'articles':articles, 'request':request})


def article(request, slug):
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        user = comment_form.save().author
        if comment_form.is_valid() and user.is_authenticated():
            Article.objects.get(slug=slug).comments.add(comment_form.save())

        else:
            return HttpResponse("You are not allowed to comment")

    else:
        comment_form = CommentForm()

    return render(request, 'article.html',
            {'article':Article.objects.get(slug=slug),'comment':comment_form,
                'request':request })


def category(request, my_category):
    article_list = Article.objects.filter(categories__name__startswith=my_category)[::-1]
    paginator = Paginator(article_list, 10)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'category.html',
        {'articles':articles,'request':request,'article_list':article_list})


def about(request,ab_var):
    return render(request, 'about.html')
