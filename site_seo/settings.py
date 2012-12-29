from django.conf import settings

ENABLED = getattr(settings, 'SITE_SEO_ENABLED', True)
COLLECT_404 = getattr(settings, 'SITE_SEO_COLLECT_404', True)
