from django.conf.urls import patterns, include, url
from article import views
from  accounts.views import register

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^article/([\w-]+)', views.article, name='article'),
    url(r'^category/([\w-]+)', views.category, name='category'),
    url(r'^login_view/', views.login_view, name='login_view'),
    url(r'^accounts/register/$',register, name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
