# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from rbac.models import User
from rbac.service.deal_session import initial_session


def login(request):
    if request.method=="POST":
        # 认证
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user=User.objects.filter(name=user,password=pwd).first()
        if user:
            # 登录成功
            # 保存登录用户状态信息
            request.session["user_id"]=user.pk

            # 录入权限session
            initial_session(user, request)

            return redirect("/customer/list/")

    return render(request, 'web/login.html')


