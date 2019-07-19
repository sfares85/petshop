# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=60)
	age = models.IntegerField()
	available = models.BooleanField (default = True)
	image = models.ImageField(null=True, blank=2)
	price = models.DecimalField(max_digits=5, decimal_places=3)