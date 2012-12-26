from django.conf import settings

SITE_SEO_ENABLED = getattr(settings, 'SITE_SEO_ENABLED', True)
