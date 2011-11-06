from django import template
from django.utils.safestring import mark_safe

from site_content.models import SiteBlock, SitePosition

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
    
    except SitePosition.DoesNoteExist:
        siteposition = SitePosition()
        
    return {'siteposition': siteposition}