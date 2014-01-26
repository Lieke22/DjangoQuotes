from django.conf.urls import patterns, url

from quotes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<quote_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<quote_id>\d+)/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<quote_id>\d+)/$', views.vote, name='vote')
)