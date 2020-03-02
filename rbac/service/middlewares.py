# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from rbac.models import Permission
import re


class PermissionMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        current_path = request.path

        # 设置白名单放行
        for reg in ["/login/","/admin/*",'/distribute/permissions/','/permissions_tree/']:
            ret = re.search(reg, current_path)
            if ret:
                return None
        # /customers/edit/1

        # 校验是否登录
        user_id=request.session.get("user_id")
        if not user_id:
            return redirect("/login/")

        # 校验权限
        permission_list=request.session.get("permission_list")

        # 路径导航列表
        request.breadcrumb = [
            {
                'title': '首页',
                'url': '/'
            }
        ]
        for item in permission_list:
            reg = "^%s$"%item['url']
            ret = re.search(reg, current_path)
            if ret:
                show_id = item['pid'] or item['id']
                request.show_id = show_id

                # 确定面包屑列表
                if item['pid']:
                    ppermission = Permission.objects.filter(pk=item['pid']).first()
                    request.breadcrumb.extend([
                        # 父列表
                        {
                             'title': ppermission.title,
                             'url': ppermission.url
                        },
                        {
                             'title': item['title'],
                             'url': request.path
                        }
                    ])
                else:
                    request.breadcrumb.append({
                         'title': item['title'],
                         'url': item['url']
                    })
                return None
        return HttpResponse("无访问权限！")
