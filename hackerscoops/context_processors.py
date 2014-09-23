from article.models import Article
from django.utils.timezone import timedelta
from unchained import wise_datetime_now

def extra_context(request):

    two_days_ago = wise_datetime_now()-timedelta(days=2)
    recent_articles = Article.objects.filter(pub_date__gte=two_days_ago).all()

    return {'recent_articles':recent_articles,}
