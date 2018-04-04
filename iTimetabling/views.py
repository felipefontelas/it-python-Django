# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Instituicao

# Create your views here.

def instituicao_list(request):
    instituicoes = Instituicao.objects.all().order_by('created_at')
    return render(request, 'iTimetabling/instituicao_list.html', {'instituicoes': instituicoes})

def instituicao_detail(request, pk):
    instituicao = get_object_or_404(Instituicao, pk=pk)
    return render(request, 'iTimetabling/instituicao_detail.html', {'instituicao': instituicao})