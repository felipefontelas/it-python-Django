# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def instituicao_list(request):
    return render(request, 'iTimetabling/instituicao_list.html', {})
