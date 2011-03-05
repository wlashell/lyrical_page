from django import template
from django.utils.safestring import mark_safe

from lyrical_page.models import SiteBlock

register = template.Library()

@register.simple_tag
def get_block(code):
    try:
        block = SiteBlock.objects.get(code=code)
        retval = block.data
        
    except SiteBlock.DoesNotExist:
        retval = ''
    
    return mark_safe(retval)
