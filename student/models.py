# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class College(models.Model):
	title=models.TextField()
	reviews=models.TextField()
	fees=models.IntegerField()
	exam=models.CharField(max_length=255)
	score=models.IntegerField()
	specialisation=models.TextField()
	location=models.TextField()