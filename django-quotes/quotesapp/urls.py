from django.conf.urls import patterns, include, url

from django.contrib import admin
from quotes import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),

    url(r'^quotes/', include('quotes.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
