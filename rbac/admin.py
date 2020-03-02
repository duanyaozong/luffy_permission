# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rbac import models

# Register your models here.


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'menu']
    search_fields = ['title']


admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(models.User)
admin.site.register(models.Menu)



