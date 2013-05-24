# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from models import ReadData

def data(request):
    read_data_list = ReadData.objects.all()
    return render_to_response('data.html', {'read_data_list': read_data_list})

