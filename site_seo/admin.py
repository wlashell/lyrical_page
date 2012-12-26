from django.contrib.admin import site, ModelAdmin

from site_seo.models import SiteUrl


class SiteUrlAdmin(ModelAdmin):
    list_display = ('site', 'url', 'page_title')
    list_editable = ('page_title',)

site.register(SiteUrl, SiteUrlAdmin)
