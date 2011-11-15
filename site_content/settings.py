from django.conf import settings

ENABLE_BUILTIN_MEDIA = getattr(settings, 'LYRICAL_PAGE_ENABLE_BUILTIN_MEDIA', True)
URL_MEDIA = getattr(settings, 'LYRICAL_PAGE_URL_MEDIA', '/static/lyrical/')

RTE_CONFIG_URI = getattr(settings, "SITE_CONTENT_RTE_CONFIG_URI", settings.STATIC_URL + 'site_content/js/lyrical_pageTinyMCEAdmin.js')