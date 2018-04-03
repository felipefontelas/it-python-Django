# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Instituicao

# Create your views here.

def instituicao_list(request):
    instituicoes = Instituicao.objects.all().order_by('created_at')
    return render(request, 'iTimetabling/instituicao_list.html', {'instituicoes': instituicoes})
