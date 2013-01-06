from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache

from site_seo.settings import ENABLED, COLLECT_404
from site_seo.common import add_404_url
from site_seo.models import SiteUrl, SiteUrlDefaults


class SiteSeoMiddleware(object):
    # FIXME: This absolutely must be refactored before release.
    # Development code ONLY
    def process_request(self, request):
        current_site = Site.objects.get_current()

        url = request.path_info

        if not url == '/':
            if not url.endswith('/') and settings.APPEND_SLASH:
                url = '%s/' % url
            if not url.startswith('/'):
                url = '/%s' % url

        try:
            siteurl = SiteUrl.objects.get(site=current_site, url=url)

        except SiteUrl.DoesNotExist:
            try:
                siteurl = SiteUrlDefaults.objects.get(site=current_site)

            except SiteUrlDefaults.DoesNotExist:
                siteurl = SiteUrl(page_title='',
                                  page_keywords='',
                                  page_description='')

        request.site_seo = {'seo_title': siteurl.page_title,
                            'seo_keywords': siteurl.page_keywords,
                            'seo_description': siteurl.page_description}

    def process_response(self, request, response):
        if response.status_code == 404 and COLLECT_404 and 'site_content' not in settings.INSTALLED_APPS:
            add_404_url(request)

        return response
