# -*- coding: utf-8 -*-
from django import forms
from .models import Instituicao

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ('nomeInstituicao', 'licencaInstituicao')
    

    def __init__(self, *args, **kwargs):
        super(InstituicaoForm, self).__init__(*args, **kwargs)
        self.fields['nomeInstituicao'].widget.attrs.update({'class': 'form-control'})
        self.fields['licencaInstituicao'].widget.attrs.update({'class': 'form-control'})
        self.fields['nomeInstituicao'].label = "Nome da Instituição"
        self.fields['licencaInstituicao'].label = "Licença da Instituição"
        
        
        