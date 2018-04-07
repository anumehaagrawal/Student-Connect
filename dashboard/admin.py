# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Counsellor, College, User, Passout

# Register your models here.
admin.site.register(Passout)
admin.site.register(Counsellor)
admin.site.register(College)
admin.site.register(User)
