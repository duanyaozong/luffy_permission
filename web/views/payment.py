# -*- coding:utf-8 -*-
import re
from django.shortcuts import render, redirect
from web import models
from web.forms.payment import PaymentForm


def payment_list(request):
    """
    付费列表
    """
    data_list = models.Payment.objects.all()
    return render(request, 'web/payment_list.html', {'data_list': data_list})


def payment_add(request):
    """
    新增付费记录
    """
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, 'web/payment_edit.html', {'form': form})
    form = PaymentForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'web/payment_edit.html', {'form': form})


def payment_edit(request, pid):
    """
    编辑付费记录
    """
    obj = models.Payment.objects.get(id=pid)
    if request.method == 'GET':
        form = PaymentForm(instance=obj)
        return render(request, 'web/payment_add.html', {'form': form})
    form = PaymentForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'web/payment_add.html', {'form': form})


def payment_del(request, pid):
    """
    删除付费记录
    """
    models.Payment.objects.filter(id=pid).delete()
    return redirect('/payment/list/')