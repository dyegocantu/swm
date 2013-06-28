# -*- coding: utf-8 -*-

import time
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import ReadData
from forms import FormPeriod

@login_required
def home(request):
    try:
        read_data = ReadData.objects.latest('pk')
    except ReadData.DoesNotExist:
        read_data = None
    return render_to_response('main/index.html', {'read_data': read_data})

@login_required
def charts(request):
    if request.method == 'POST':
        form = FormPeriod(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            read_data_list = \
                ReadData.objects.filter(created__range= \
                (data['start_date'], data['end_date']))
            data = []
            for item in read_data_list:
                data.append([int(time.mktime(item.created.timetuple())*1000), \
                        item.temperature])
            return render_to_response('charts/charts.html', {'data': data})
    else:
        form = FormPeriod()
    return render_to_response('charts/form.html', {'form': form}, \
            context_instance=RequestContext(request))

@login_required
def reports(request):
    if request.method == 'POST':
        form = FormPeriod(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            read_data_list = \
                ReadData.objects.filter(created__range=\
                (data['start_date'], data['end_date']))
            return render_to_response('reports/reports.html', \
                    {'read_data_list': read_data_list})
    else:
        form = FormPeriod()
    return render_to_response('reports/form.html', {'form': form}, \
            context_instance=RequestContext(request))

