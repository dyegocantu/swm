# -*- coding: utf-8 -*-

import time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from main.models import ReadData

def items():
    data = ReadData.objects.all()
    items = {'charts': {'temperature': [], 'humidity': []}}
    for item in data:
        created = int(time.mktime(item.created.timetuple())*1000)
        items['charts']['temperature'].append([created, item.temperature])
        items['charts']['humidity'].append([created, item.humidity])
    return simplejson.dumps(items)

@login_required
def charts(request):
    return render_to_response('charts/charts.html', {'data': items()})

def charts_ajax(request):
    return HttpResponse(items(), content_type='application/json')

