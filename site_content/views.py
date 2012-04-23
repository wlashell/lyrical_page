from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.views.decorators.csrf import requires_csrf_token

from site_content.models import SitePage, SiteBlock, SiteMenuItem, SiteMenu, SitePageAlias

@requires_csrf_token
def site_page(request, url, extra_context=None):
    if not url == '/':
        if not url.endswith('/') and settings.APPEND_SLASH:
            url = '%s/' % url
        if not url.startswith('/'):
            url = '/%s' % url

    sitepage = None    

    if url == '/':
        try:
            sitepage = SitePage.objects.get(is_index=True, site__id=settings.SITE_ID)
        except SitePage.DoesNotExist:
            pass
        
    if not sitepage:
        try:
            sitepage = SitePage.objects.get(url=url, site__id=settings.SITE_ID)
        except SitePage.DoesNotExist:
            pass
    if not sitepage:
        try:
            sitepage = SitePage.objects.get(sitepagealias__url_alias=url)
        except SitePage.DoesNotExist:
            pass

    if not sitepage:
        try:
            redirect_path = SitePage.objects.get(sitepageredirect__url=url)
            return HttpResponseRedirect(redirect_path.url)
        except SitePage.DoesNotExist:
            raise Http404
    
    if not sitepage:
        raise Http404
 
    if sitepage.template:
        template_path = sitepage.template
    else:
        template_path = 'site_content/site_page.html'
    
    if sitepage.login_required and not request.user.is_authenticated():
        return redirect_to_login(request.path)
    
    context_dict = {'sitepage': sitepage, 'request_path': request.path}
    if extra_context:
        context_dict = dict(context_dict, **extra_context)
        
    return direct_to_template(request,
                              template_path,
                              context_dict)
