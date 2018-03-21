# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import College, Counsellor
from django.contrib import admin

# Register your models here.
admin.site.register(College)
admin.site.register(Counsellor)
