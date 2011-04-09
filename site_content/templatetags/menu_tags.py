from django import template

from site_content.models import SiteMenu, SiteMenuItem, SitePage

register = template.Library()

@register.inclusion_tag('lyrical_page/tag_nav.html')
def get_menu(code, current='', show_label='True'):
    try:
        menu = SiteMenu.objects.get(code=code)
    except SiteMenu.DoesNotExist:
        return {}
	
    items = []
    mitems = SiteMenuItem.objects.filter(sitemenu=menu)
    for mitem in mitems:
        items.insert(mitem.weight, {'url': mitem.url, 'weight': mitem.weight, 'label': mitem.label})
        
    mitems = SitePage.objects.filter(sitemenu=menu).order_by('sitemenu_weight')
    for mitem in mitems:
        items.insert(mitem.sitemenu_weight, {'url':mitem.url, 'weight': mitem.sitemenu_weight, 'label': mitem.sitemenu_label})
    
    return {'items': items, 'current': current, 'code': code, 'menu': menu, 'show_label': show_label}    

@register.inclusion_tag('lyrical_page/tag-global-nav.html')
def global_nav(current=''):
    menu = SiteMenu.objects.get(code='global-nav')
    
    items = []
    mitems = SiteMenuItem.objects.filter(sitemenu=menu)
    for mitem in mitems:
        items.insert(mitem.weight, {'url': mitem.url, 'weight': mitem.weight, 'label': mitem.label})
        
    mitems = SitePage.objects.filter(sitemenu=menu).order_by('sitemenu_weight')
    for mitem in mitems:
        items.insert(mitem.sitemenu_weight, {'url':mitem.url, 'weight': mitem.sitemenu_weight, 'label': mitem.sitemenu_label})
        
    return {'items': items, 'current': current }

@register.inclusion_tag('lyrical_page/global_menu.html')
def global_nav_menu_left(current=''):
    sitemenu = SiteMenu.objects.get(code='global-nav-menu-left')
    
    retval = []
    mitems = SiteMenuItem.objects.filter(sitemenu=sitemenu).order_by('weight')
    for mitem in mitems:
        if mitem.url == '/' and current == '/index/':
            current = '/'
            
        retval.insert(mitem.weight, {'url': mitem.url, 'label': mitem.label, 'is_page': False, 'weight' : mitem.weight})
    
    mitems = SitePage.objects.filter(sitemenu=sitemenu)
    for mitem in mitems:
        retval.insert(mitem.sitemenu_weight, {'url': mitem.url, 'label': mitem.sitemenu_label, 'is_page': True, 'weight': mitem.sitemenu_weight})
    
    return {'mitems': retval, 'current': current, 'menu_column' : 'left' }

@register.inclusion_tag('lyrical_page/global_menu.html')
def global_nav_menu_right(current=''):
    sitemenu = SiteMenu.objects.get(code='global-nav-menu-right')
    
    retval = []
    mitems = SiteMenuItem.objects.filter(sitemenu=sitemenu).order_by('weight')
    for mitem in mitems:
        retval.insert(mitem.weight, {'url': mitem.url, 'label': mitem.label, 'is_page': False, 'weight' : mitem.weight})
    
    mitems = SitePage.objects.filter(sitemenu=sitemenu)
    for mitem in mitems:
        retval.insert(mitem.sitemenu_weight, {'url': mitem.url, 'label': mitem.sitemenu_label, 'is_page': True, 'weight': mitem.sitemenu_weight})
    
    return {'mitems': retval, 'current': current, 'menu_column' : 'right' }

@register.inclusion_tag('lyrical_page/global_menu_footer.html')
def global_footer():
    sitemenus = SiteMenu.objects.filter(code__in=['global-nav-menu-left','global-nav-menu-right', 'footer'])
    
    retval = []
    mitems = SiteMenuItem.objects.filter(sitemenu__in=sitemenus).order_by('weight')
    for mitem in mitems:
        retval.insert(mitem.weight, {'url': mitem.url, 'label': mitem.label, 'is_page': False, 'weight' : mitem.weight})
        
    mitems = SitePage.objects.filter(sitemenu=sitemenus)
    for mitem in mitems:
        retval.insert(mitem.sitemenu_weight, {'url': mitem.url, 'label': mitem.sitemenu_label, 'is_page': True, 'weight': mitem.sitemenu_weight})
    
    return {'mitems': retval}
