from django import template

register = template.Library()

from django.conf import settings
import re


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    permission_menu_dict = request.session.get('permission_menu_dict')
    return {"permission_menu_dict": permission_menu_dict}


@register.simple_tag
def gen_role_url(request, rid):
    params = request.GET.copy()
    params._mutable = True
    params['rid'] = rid
    return params.urlencode()
