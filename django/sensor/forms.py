# -*- coding: utf-8 -*-

from django import forms

class FormPeriod(forms.Form):
    start_date = forms.DateField(label='Inicio', \
            widget=forms.DateInput(format='%d/%m/%Y'), \
            input_formats=['%d/%m/%y', '%d/%m/%Y'])
    end_date = forms.DateField(label='Fim', \
            widget=forms.DateInput(format='%d/%m/%Y'), \
            input_formats=['%d/%m/%y', '%d/%m/%Y'])

