# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField(to='Role', verbose_name='用户所拥有的角色', blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField(to='Permission', verbose_name='角色所拥有的权限', blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=32, verbose_name='权限')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=32, verbose_name='url别名',default='')
    pid = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, verbose_name='父权限')

    class Meta:
        verbose_name_plural = '权限表'
        verbose_name = '权限表'

    def __str__(self):
        return self.title


class Menu(models.Model):
    """
    菜单表
    """
    title = models.CharField(max_length=32, verbose_name='菜单')
    icon = models.CharField(max_length=32, verbose_name='图标', null=True, blank=True)

    def __str__(self):
        return self.title
