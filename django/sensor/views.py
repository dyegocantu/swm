# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from models import ReadData

def data(request):
    read_data = ReadData.objects.latest('pk')
    return render_to_response('data.html', {'read_data': read_data})

