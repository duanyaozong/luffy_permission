# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    客户表
    """
    name = models.CharField(max_length=32, verbose_name='姓名')
    age = models.CharField(max_length=32, verbose_name='年龄')
    email = models.EmailField(max_length=32, verbose_name='邮箱')
    company = models.CharField(max_length=32, verbose_name='公司')

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
    付费记录
    """
    customer = models.ForeignKey(verbose_name='关联客户', to='Customer', on_delete=models.CASCADE)
    money = models.IntegerField(verbose_name='付费金额')
    create_time = models.DateTimeField(verbose_name='付费时间', auto_now_add=True)
