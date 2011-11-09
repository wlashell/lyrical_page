from django import template
from django.utils.safestring import mark_safe

from site_content.models import SiteBlock, SitePage, SitePosition, SitePagePositionBlock

register = template.Library()

@register.simple_tag
def get_block(code):
    try:
        block = SiteBlock.objects.get(code=code)
        retval = block.data
        
    except SiteBlock.DoesNotExist:
        retval = ''
    
    return mark_safe(retval)

@register.inclusion_tag('site_content/siteposition_siteblock.html')
def get_position_blocks(position):
    try:
        siteposition = SitePosition.objects.get(code=position)
    
    except SitePosition.DoesNotExist:
        siteposition = SitePosition()
        
    return {'siteposition': siteposition}

@register.inclusion_tag('site_content/siteposition_sitepageblocks.html')
def get_page_position_blocks(page, position):
    try:
        sitepageposition = SitePagePositionBlock.objects.get(sitepage__id=page, siteposition__code=position)
    except (SitePagePositionBlock.DoesNotExist, SitePosition.DoesNotExist, SitePage.DoesNotExist):
    
        sitepageposition = None
            
    return {'sitepageposition':sitepageposition}