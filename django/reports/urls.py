from django.conf.urls import patterns, url
from reports.views import *

urlpatterns = patterns(
    '',
    url(r'^$', reports),
)
