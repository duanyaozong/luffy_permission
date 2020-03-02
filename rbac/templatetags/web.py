

from django.utils.safestring import mark_safe
from django.template import Library
import re
register =Library()


@register.inclusion_tag("rbac/menu.html")
def get_menu_styles(request):
    permission_menu_dict = request.session.get("permission_menu_dict")
    # print("permission_menu_dict",permission_menu_dict)
    for val in permission_menu_dict.values():
        val['class'] = 'hide'
        for item in val['children']:
            # ret = re.search('^{}$'.format(request.path), item['url'])
            if item['id'] == request.show_id:
                val['class'] = ''
    return {"permission_menu_dict":permission_menu_dict}


@register.filter
def has_permission(btn_url, request):
    return btn_url in request.session.get('permission_names')



