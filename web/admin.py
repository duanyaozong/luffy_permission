# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web import models

# Register your models here.


admin.site.register(models.Customer)
admin.site.register(models.Payment)


