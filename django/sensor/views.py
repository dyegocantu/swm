# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import ReadData
from forms import FormPeriod

def last_data(request):
    read_data = ReadData.objects.latest('pk')
    return render_to_response('last.html', {'read_data': read_data})

def period_data(request):
    if request.method == 'POST':
        form = FormPeriod(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            read_data_list = \
            ReadData.objects.filter(created__range=(data['start_date'], \
                    data['end_date']))
            return render_to_response('chart.html', \
                    {'read_data_list': read_data_list})
    else:
        form = FormPeriod()
    return render_to_response('period.html', {'form': form}, \
            context_instance=RequestContext(request))

