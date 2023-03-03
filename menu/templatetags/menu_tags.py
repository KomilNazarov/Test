from django import template
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name).prefetch_related('children')

    def render_menu_item(menu_item):
        active = ''
        if request.path == menu_item.url:
            active = 'active'
        has_children = menu_item.children.exists()
        template = f'<li class="{active}"><a href="{menu_item.url}">{menu_item.title}</a>'
        if has_children:
            template += '<ul>'
            for child in menu_item.children.all():
                template += render_menu_item(child)
            template += '</ul>'
        template += '</li>'
        return template

    menu = ''
    for menu_item in menu_items:
        menu += render_menu_item(menu_item)

    return menu
