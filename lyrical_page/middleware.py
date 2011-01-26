from django.http import Http404
from django.conf import settings

from lyrical_page.views import site_page

class SitePageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        
        try:
            return site_page(request, request.path_info)
        
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
