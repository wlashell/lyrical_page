from django.conf import settings

ENABLE_BUILTIN_MEDIA = getattr(settings, 'LYRICAL_PAGE_ENABLE_BUILTIN_MEDIA', True)
URL_MEDIA = getattr(settings, 'LYRICAL_PAGE_URL_MEDIA', '/static/lyrical/')

# List of templates that should be available to assign to a site page
# ex: (("site_content/internal.html", "Internal Content"),
#     ("site_content/index.html", "Home Page"))
SITE_PAGE_TEMPLATES = getattr(settings, 'SITE_CONTENT_SITE_PAGE_TEMPLATES', None)
# Default template to use when creating a new page
# ex: "site_content/internal.html"
SITE_PAGE_DEFAULT_TEMPLATE = getattr(settings, 'SITE_CONTENT_SITE_PAGE_DEFAULT_TEMPLATE', None)

# URI of base Javascript file for the RTE editor
RTE_SCRIPT_URI = getattr(settings, 'SITE_CONTENT_RTE_SCRIPT_URI', settings.STATIC_URL + 'site_content/tinymce/jscripts/tiny_mce/tiny_mce.js')
# URI of config file for RTE editor
RTE_CONFIG_URI = getattr(settings, "SITE_CONTENT_RTE_CONFIG_URI", settings.STATIC_URL + 'site_content/js/lyrical_pageTinyMCEAdmin.js')
