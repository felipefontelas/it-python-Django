# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Instituicao
from .forms import InstituicaoForm
from django.shortcuts import redirect

# Create your views here.


def instituicao_list(request):
    instituicoes = Instituicao.objects.all().order_by('created_at')
    return render(request, 'iTimetabling/instituicao_list.html', {'instituicoes': instituicoes})


def instituicao_detail(request, pk):
    instituicao = get_object_or_404(Instituicao, pk=pk)
    return render(request, 'iTimetabling/instituicao_detail.html', {'instituicao': instituicao})


def instituicao_new(request):
    if request.method == 'POST':
        instituicao = InstituicaoForm(request.POST)
        if instituicao.is_valid():
            instituicao = instituicao.save(commit=False)
            instituicao.created_at = timezone.now()
            instituicao.save()
            return redirect('instituicao_detail', pk=instituicao.pk)
    else:
        instituicao = InstituicaoForm()
    return render(request, 'iTimetabling/instituicao_edit.html', {'instituicao': instituicao})

def instituicao_edit(request, pk):
    instituicao = get_object_or_404(Instituicao, pk=pk)
    if request.method == "POST":
        instituicao = InstituicaoForm(request.POST, instance=instituicao)
        if instituicao.is_valid():
            instituicao = instituicao.save(commit=False)
            instituicao.created_at = timezone.now()
            instituicao.save()
            return redirect('instituicao_detail', pk=instituicao.pk)
    else:
        instituicao = InstituicaoForm(instance=instituicao)
    return render(request, 'iTimetabling/instituicao_edit.html', {'instituicao': instituicao})

def instituicao_delete(request, pk):
    instituicao = get_object_or_404(Instituicao, pk=pk)
    instituicao.delete()
    return redirect('/')