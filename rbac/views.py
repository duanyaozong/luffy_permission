# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from rbac import models

# Create your views here.


def distribute_permissions(request):
    """
    分配权限
    :param request:
    :return:
    """
    uid = request.GET.get('uid')
    user = models.User.objects.filter(id=uid)
    rid = request.GET.get('rid')

    if request.method == 'POST' and request.POST.get('postType') == 'role':
        l = request.POST.getlist('roles')
        user.first().roles.set(l)

    if request.method == "POST" and request.POST.get('postType') == 'permission':
        l = request.POST.getlist("permissions_id")
        models.Role.objects.filter(pk=rid).first().permissions.set(l)

    # 所有用户
    user_list = models.User.objects.all()
    # user_has_roles = user.values('id', 'roles')
    role_list = models.Role.objects.all()

    if uid:
        role_id_list = models.User.objects.get(pk=uid).roles.all().values_list('pk')
        role_id_list = [item[0] for item in role_id_list]

        if rid:
            per_id_list = models.Role.objects.filter(pk=rid).values_list('permissions__pk').distinct()
        else:
            per_id_list = models.User.objects.get(pk=uid).roles.values_list('permissions__pk').distinct()

        per_id_list = [item[0] for item in per_id_list]

    return render(request, 'rbac/distribute_permissions.html', locals())


def permissions_tree(request):
    permissions = models.Permission.objects.values('pk', 'title', 'url', 'menu__title', 'menu__pk', 'pid_id')
    return JsonResponse(list(permissions), safe=False)


