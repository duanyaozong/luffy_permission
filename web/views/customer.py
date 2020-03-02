# -*- coding:utf-8 -*-
import os
import re
import mimetypes
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings

from web import models
from web.forms.customer import CustomerForm


def customer_list(request):
    """
    客户列表
    """
    data_list = models.Customer.objects.all()
    return render(request, 'web/customer_list.html', locals())


def customer_add(request):
    """
    增加客户
    """
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'web/customer_add.html', {'form': form})
    form = CustomerForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/customer/list/')
    return render(request, 'web/customer_add.html', {'form': form})


def customer_edit(request, cid):
    """
    编辑客户
    """
    obj = models.Customer.objects.get(id=cid)
    if request.method == "GET":
        form = CustomerForm(instance=obj)
        return render(request, 'web/customer_add.html', {'form': form})
    form = CustomerForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/customer/list/')
    return render(request, 'web/customer_add.html', {'form': form})


def customer_del(request, cid):
    """
    删除客户
    """
    models.Customer.objects.filter(id=cid).delete()
    return redirect('/customer/list/')