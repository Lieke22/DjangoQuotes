from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quotes.views.index', name='idex'),
    url(r'^quotes/', include('quotes.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
