from django import template

from site_content.models import SiteMenu, SiteMenuItem, SitePage

register = template.Library()

@register.inclusion_tag('site_content/tag_nav.html')
def get_menu(code, current='', show_label='True'):
    try:
        menu = SiteMenu.objects.get(code=code)
    except SiteMenu.DoesNotExist:
        return {}
    
    items = []
    mitems = SiteMenuItem.objects.filter(sitemenu=menu)
    for mitem in mitems:
        items.append({'url': mitem.url, 'weight': mitem.weight if mitem.weight else 0, 'label': mitem.label})
        
    mitems = SitePage.objects.filter(sitemenu=menu).order_by('sitemenu_weight')
    for mitem in mitems:
        items.append({'url':mitem.url, 'weight': mitem.sitemenu_weight if mitem.sitemenu_weight else 0, 'label': mitem.sitemenu_label, 'depth': mitem.sitemenu_depth if mitem.sitemenu_depth else 0})
    
    if items:
        items = sorted(items, key=lambda k: k['weight'])
    
    return {'items': items, 'current': current, 'code': code, 'menu': menu, 'show_label': show_label}
