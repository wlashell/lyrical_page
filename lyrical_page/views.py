from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

from lyrical_page.models import SitePage, SiteBlock, SiteMenuItem, SiteMenu

def site_page(request, url, extra_context=None):
    if not url == '/':
        if not url.endswith('/') and settings.APPEND_SLASH:
            url = '%s/' % url
        if not url.startswith('/'):
            url = '/%s' % url
            
    sitepage = get_object_or_404(SitePage, url=url)
    
    if sitepage.template:
        template_path = sitepage.template
    else:
        template_path = 'lyrical_page/site_page.html'
    
    
    context_dict = {'sitepage': sitepage}
    if extra_context:
        context_dict = dict(context_dict, **extra_context)
        
    return direct_to_template(request,
                              template_path,
                              context_dict)
