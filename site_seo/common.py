from django.conf import settings
from django.contrib.sites.models import Site

from site_seo.settings import COLLECT_404
from site_seo.models import SiteUrl404


def add_404_url(request):
    if COLLECT_404:
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

    return True
