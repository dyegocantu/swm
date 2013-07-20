# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import ReadData

@login_required
def index(request):
    try:
        read_data = ReadData.objects.latest('pk')
    except ReadData.DoesNotExist:
        read_data = None
    return render_to_response('main/index.html', {'read_data': read_data})

