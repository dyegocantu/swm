# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import ReadData
from forms import FormPeriod

@login_required
def last_data(request):
    try:
        read_data = ReadData.objects.latest('pk')
    except ReadData.DoesNotExist:
        read_data = None
    return render_to_response('last.html', {'read_data': read_data})

@login_required
def period_data(request):
    if request.method == 'POST':
        form = FormPeriod(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            read_data_list = \
            ReadData.objects.filter(created__range=(data['start_date'], \
                    data['end_date']))
            return render_to_response('period_result.html', \
                    {'read_data_list': read_data_list})
    else:
        form = FormPeriod()
    return render_to_response('period.html', {'form': form}, \
            context_instance=RequestContext(request))

