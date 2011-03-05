from django.conf import settings

ENABLE_BUILTIN_MEDIA = getattr(settings, 'LYRICAL_PAGE_ENABLE_BUILTIN_MEDIA', True)
URL_MEDIA = getattr(settings, 'LYRICAL_PAGE_URL_MEDIA', '/static/lyrical/')

