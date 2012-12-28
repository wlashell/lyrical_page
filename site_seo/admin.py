from django.contrib.admin import site, ModelAdmin

from site_seo.models import SiteUrl, SiteUrlDefaults, SiteUrl404


class SiteUrlAdmin(ModelAdmin):
    list_display = ('site', 'url', 'page_title')
    list_editable = ('page_title',)

site.register(SiteUrl, SiteUrlAdmin)


class SiteUrlDefaultsAdmin(ModelAdmin):
    list_display = ('site',)

site.register(SiteUrlDefaults, SiteUrlDefaultsAdmin)


class SiteUrl404Admin(ModelAdmin):
    list_display = ('site', 'url', 'date_created', 'hit_cnt')

site.register(SiteUrl404, SiteUrl404Admin)
