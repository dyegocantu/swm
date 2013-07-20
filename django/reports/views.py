# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from main.models import ReadData
from forms import FormPeriod

@login_required
def reports(request):
    if request.method == 'POST':
        form = FormPeriod(request.POST, request.FILES)
        if form.is_valid():
            period = form.cleaned_data
            read_data_list = \
                ReadData.objects.filter(created__range=\
                (period['start_date'], period['end_date']))
            return render_to_response('reports/reports.html', \
                    {'read_data_list': read_data_list})
    else:
        form = FormPeriod()
    return render_to_response('reports/form.html', {'form': form}, \
            context_instance=RequestContext(request))

