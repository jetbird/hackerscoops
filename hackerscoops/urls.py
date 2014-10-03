from django.conf.urls import patterns, include, url
from django.conf import settings
from article import views
from  accounts.views import register, user_login, user_logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^article/([\w-]+)', views.article, name='article'),
    url(r'^category/([\w-]+)', views.category, name='category'),
    url(r'^accounts/register/$',register, name='register'),
    url(r'^accounts/login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/([\w-]+)', views.about, name='about')
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',{
                'document_root':settings.MEDIA_ROOT}))
