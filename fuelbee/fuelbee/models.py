# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class Dealer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Price(models.Model):
    state = models.MultiSelectField(choices=STATES)
    dealer = models.ChoiceField(model=Dealer)
    petrol = models.FloadField()
    diesel = models.FloatField()

    
