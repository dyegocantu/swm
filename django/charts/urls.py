from django.conf.urls import patterns, url
from charts.views import *

urlpatterns = patterns(
    '',
    url(r'^$', charts),
    url(r'^charts_ajax/$', charts_ajax),
)
