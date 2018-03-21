# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class College(models.Model):
	title = models.CharField(max_length=255)
	reviews = models.CharField(max_length=1000)
	fees = models.CharField(max_length=255)
	exam = models.CharField(max_length=255)
	score = models.CharField(max_length=255)
	specialisation = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	ethnicity = models.CharField(max_length=255)
	ratings = models.IntegerField()

class Counsellor(models.Model):
	name = models.CharField(max_length=255)
	university = models.CharField(max_length=255)
	contact = models.CharField(max_length=255)
