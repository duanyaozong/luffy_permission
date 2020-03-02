# -*- coding:utf-8 -*-
from rbac.models import Role


def initial_session(user, request):
    """
    功能：将当前登录人的所有权限录入session中
    :param user: 当前登录人
    """
    # 查询当前登录人的所有权限列表
    # 查看当前登录人的所有角色
    # ret=Role.objects.filter(user=user)
    permissions = Role.objects.filter(user=user).values("permissions__url",
                                                        "permissions__title",
                                                        "permissions__name",
                                                        "permissions__pk",
                                                        "permissions__pid",
                                                        "permissions__menu__title",
                                                        "permissions__menu__icon",
                                                        "permissions__menu__pk").distinct()

    permission_list = []
    permission_names = []
    permission_menu_dict ={}

    for item in permissions:
        # 构建权限列表
        permission_list.append({
            'url': item["permissions__url"],
            'title': item['permissions__title'],
            'id': item['permissions__pk'],
            'pid': item['permissions__pid'],
        })
        permission_names.append(item["permissions__name"])

        # 菜单权限
        menu_pk=item["permissions__menu__pk"]
        if menu_pk:
            if menu_pk not in permission_menu_dict:
                permission_menu_dict[menu_pk]={
                     "menu_title": item["permissions__menu__title"],
                     "menu_icon": item["permissions__menu__icon"],
                     "children": [
                         {
                             "title": item["permissions__title"],
                             "url": item["permissions__url"],
                             'id': item['permissions__pk']
                         }
                     ],

                }
            else:
                permission_menu_dict[menu_pk]["children"].append({
                    "title": item["permissions__title"],
                    "url": item["permissions__url"],
                    'id': item['permissions_pk']
                })

    # permission_menu_list:
    '''
    元数据：
     [  {
            'permissions__url': '/customer/list/',
            'permissions__title': '客户列表',
            'permissions__menu__title': '信息管理',
            'permissions__menu__icon': 'fa fa-connectdevelop',
            'permissions__menu__pk': 1
        },  
        
        {
            'permissions__url': '/mycustomer/',
            'permissions__title': '我的私户',
            'permissions__menu__title': '信息管理',
            'permissions__menu__icon': 'fa fa-connectdevelop',
            'permissions__menu__pk': 1
        },  
        
        {
            'permissions__url': '/payment/list/',
            'permissions__title': '缴费列表',
            'permissions__menu__title': '财务管理',
            'permissions__menu__icon': 'fa fa-code-fork',
            'permissions__menu__pk': 2
        }, ]
    
    目标数据：
    {
       1:{
            "title":"信息管理",
            "icon":"",
            "children":[
                {
                  "title":"客户列表",
                  "url":"",
                }
            ]
            
          },
          
       2:{
            "title":"财务管理",
            "icon":"",
            "children":[
                {
                  "title":"缴费列表",
                  "url":"",
                },
            ]
        }, 
    }
    
  permission_menu_dict= {
        1:{
            "title":"信息管理",
            "icon":"",
            "children":[
                {
                  "title":"客户列表",
                  "url":"",
                },
                 {
                  "title":"我的私户",
                  "url":"",
                 },
            ]
            
        },
          
        2:{
            "title":"财务管理",
            "icon":"",
            "children":[
                {
                  "title":"缴费列表",
                  "url":"",
                },
            ]
            
        }, 
       }  
    '''
    # 将当前登录人的权限列表注入session中
    request.session["permission_list"] = permission_list
    request.session["permission_names"] = permission_names
    # 将当前登录人的菜单权限字典注入session中
    request.session["permission_menu_dict"] = permission_menu_dict

    # 将当前登录人的权限列表注入session中
    request.session["permission_list"] = permission_list
    # 将当前登录人的菜单权限字典注入session中
    request.session["permission_menu_dict"] = permission_menu_dict