import os

from django.conf import settings

ENABLED = getattr(settings, 'SITE_CONTENT_ENABLED', True)

# helper paths
SITE_CONTENT_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_CONTENT_DOC_ROOT = os.path.join(SITE_CONTENT_ROOT, 'doc')

ENABLE_BUILTIN_MEDIA = getattr(settings, 'LYRICAL_PAGE_ENABLE_BUILTIN_MEDIA', True)
URL_MEDIA = getattr(settings, 'LYRICAL_PAGE_URL_MEDIA', '/static/lyrical/')

RTE_CONFIG_URI = getattr(settings, "SITE_CONTENT_RTE_CONFIG_URI", settings.STATIC_URL + 'site_content/js/lyrical_pageTinyMCEAdmin.js')

# The following files are configured to be installed by the  sitecontentcopystatic
# management command.

STATICFILES_TO_COPY = {'css': ('main.css',),
                       'js': ('main.js',
                              'plugins.js',)
                       }
