from django.conf.urls import patterns, include, url
from article import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^article/([\w-]+)', views.article, name='article'),
    url(r'^category/([\w-]+)', views.category, name='category'),
    url(r'^admin/', include(admin.site.urls)),
)
