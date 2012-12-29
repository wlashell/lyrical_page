from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache

from site_seo.models import SiteUrl, SiteUrl404


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
            siteurl = SiteUrl()

        request.site_seo = {'seo_title': siteurl.page_title,
                            'seo_keywords': siteurl.page_keywords,
                            'seo_description': siteurl.page_description}

    def process_response(self, request, response):
        if response.status_code == 404:
            try:
                siteurl404 = SiteUrl404.objects.get(url=request.path_info)
                siteurl404.hit_cnt += 1
                siteurl404.save()

            except SiteUrl404.DoesNotExist:
                site = Site.objects.get_current()
                siteurl404 = SiteUrl404()
                siteurl404.url = request.path_info
                siteurl404.site = site
                siteurl404.hit_cnt = 1
                siteurl404.save()

        return response
