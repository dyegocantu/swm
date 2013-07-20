# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.home'),
    url(r'^charts/', include('charts.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', \
            {'template_name': 'login/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', \
            {'login_url': '/login/'}),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', \
                {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', \
                {'document_root': settings.STATIC_ROOT}),
)

