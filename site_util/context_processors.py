import datetime
import string

from django.contrib.sites.models import Site

def site(request):
    site_info = {'site_name': 'Name Not Set', 'LETTERS_UPPER': string.uppercase}

    if Site._meta.installed:
        site_info['site_name'] = Site.objects.get_current().name
        site_info['site_id'] = Site.objects.get_current().id
    return site_info
