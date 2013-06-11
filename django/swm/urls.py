# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swm.views.home', name='home'),
    # url(r'^swm/', include('swm.foo.urls')),
    
    url(r'^$', 'main.views.home'),
    url(r'^charts/$', 'main.views.charts'),
    url(r'^reports/$', 'main.views.reports'),
    url(r'^login/$', 'django.contrib.auth.views.login', \
            {'template_name': 'login/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', \
            {'login_url': '/login/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', \
                {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', \
                {'document_root': settings.STATIC_ROOT}),
)

