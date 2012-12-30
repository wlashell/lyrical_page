from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.http import Http404

from site_content.views import site_page


def make_tls_property(default=None):
    """Creates a class-wide instance property with a thread-specific value."""
    class TLSProperty(object):
        def __init__(self):
            from threading import local
            self.local = local()

        def __get__(self, instance, cls):
            if not instance:
                return self
            return self.value

        def __set__(self, instance, value):
            self.value = value

        def _get_value(self):
            return getattr(self.local, 'value', default)

        def _set_value(self, value):
            self.local.value = value
        value = property(_get_value, _set_value)

    return TLSProperty()

_default_site_id = getattr(settings, 'SITE_ID', None)
SITE_ID = settings.__class__.SITE_ID = make_tls_property()


class SitePageFallbackMiddleware(object):
    def process_request(self, request):
        # Ignore port if it's 80 or 443
        if ':' in request.get_host():
            domain, port = request.get_host().split(':')
            if int(port) not in (80, 443, 8080):
                domain = request.get_host()
        else:
            domain = request.get_host().split(':')[0]

        # Domains are case insensitive
        domain = domain.lower()

        # We cache the SITE_ID
        cache_key = 'LyricalPage:Site:domain:%s' % domain
        site = cache.get(cache_key)
        if site:
            SITE_ID.value = site
        else:
            try:
                site = Site.objects.get(domain=domain)
            except Site.DoesNotExist:
                site = None

            if not site:
                # Fall back to with/without 'www.'
                if domain.startswith('www.'):
                    fallback_domain = domain[4:]
                else:
                    fallback_domain = 'www.' + domain

                try:
                    site = Site.objects.get(domain=fallback_domain)
                except Site.DoesNotExist:
                    site = None

            # Add site if it doesn't exist
            if not site and getattr(settings, 'CREATE_SITES_AUTOMATICALLY',
                                    False):
                site = Site(domain=domain, name=domain)
                site.save()

            # Set SITE_ID for this thread/request
            if site:
                SITE_ID.value = site.pk
            else:
                SITE_ID.value = _default_site_id

            cache.set(cache_key, SITE_ID.value, 5 * 60)

    def process_response(self, request, response):
        if response.status_code != 404:
            return response

        try:
            return site_page(request, request.path_info)

        except Http404:
            if 'site_seo' in settings.INSTALLED_APPS:
                import site_seo.common
                site_seo.common.add_404_url(request)

            return response
        except:
            if settings.DEBUG:
                raise

            return response
