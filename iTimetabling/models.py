# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Instituicao(models.Model):
    nomeInstituicao = models.CharField(max_length = 200)
    licencaInstituicao = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def store(self):
        self.save()

    def __str__(self):
        return self.nomeInstituicao