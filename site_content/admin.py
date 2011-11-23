from django.conf import settings
from django.contrib.admin import site, ModelAdmin, StackedInline, TabularInline

from site_content.settings import ENABLE_BUILTIN_MEDIA, RTE_CONFIG_URI
from site_content.models import SitePage, SiteMenu, SiteMenuItem, SiteBlock, SitePageAlias, SitePageRedirect, SitePosition, SitePagePositionBlock

class SitePageAliasInline(StackedInline):
    model = SitePageAlias
    classes = ('collapse-open',)
    allow_add = True
    extra = 0

class SitePageRedirectInline(StackedInline):
    model = SitePageRedirect
    classes = ('collapse-open',)
    allow_add = True
    extra = 0
    
class SitePagePositionBlockInline(TabularInline):
    model = SitePagePositionBlock
    fields = ('siteposition','siteblocks','weight')
    allow_add = True
    extra = 0

class SitePageAdmin(ModelAdmin):
    list_display = ('url', 'content_header', 'sitemenu', 'sitemenu_label', 'sitemenu_weight', 'sitemenu_depth', 'template', 'site')
    list_filter = ('sitemenu', 'site')
    list_editable = ('sitemenu', 'sitemenu_label', 'sitemenu_weight', 'sitemenu_depth', 'template')
    save_on_top = True
    inlines = (SitePageAliasInline,SitePageRedirectInline,SitePagePositionBlockInline)
    ordering = ('sitemenu','sitemenu_weight','url',)
    
    fieldsets = (
        (None, {'fields': ('site', 'is_index', 'url', 'title', 'content_header', 'content')}),
        ('Menu', {'fields': ('sitemenu', 'sitemenu_label', 'sitemenu_weight', 'sitemenu_depth')}),
        ('Meta Tags', {'classes': ('collapse closed',), 'fields': ('meta_description', 'meta_keywords')}),
        ('Advanced', {'classes': ('collapse closed',), 'fields': ('page_class', 'template')})
    )
    
    if ENABLE_BUILTIN_MEDIA:
        class Media:
            js = (getattr(settings, 'STATIC_URL', '') + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', RTE_CONFIG_URI)
            css = {'all':('site_content/css/grappelli-tinymce.css',)}
        
    def __unicode__(self):
        return '%s' % 'administration'
        
site.register(SitePage, SitePageAdmin)

class SiteMenuItemAdmin(ModelAdmin):
    list_display = ('label', 'weight', 'url', 'sitemenu')
    list_filter = ('sitemenu',)
    list_editable = ('weight',)
    ordering = ('weight',)

    def __unicode__(self):
        return '%s' % 'administration'

site.register(SiteMenuItem, SiteMenuItemAdmin)

class SiteMenuAdmin(ModelAdmin):
    list_display = ('label', 'code', 'weight')
    ordering = ('weight',)

    def __unicode__(self):
        return '%s' % 'administration'
    
site.register(SiteMenu, SiteMenuAdmin)

class SiteBlockAdmin(ModelAdmin):
    save_on_top = True
    list_display = ('code', 'css_class', 'siteposition', 'weight',)
    list_editable = ('css_class', 'siteposition', 'weight',)
    list_filter = ('siteposition',)
    class Media:
        js = (getattr(settings, 'STATIC_URL', '') + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', RTE_CONFIG_URI)

    def __unicode__(self):
        return '%s' % 'administration'

site.register(SiteBlock, SiteBlockAdmin)

class SitePageRedirect(ModelAdmin):
    list_display = ('sitepage', 'url')
    save_on_top = True

class SitePositionAdmin(ModelAdmin):
    save_on_top = True
    list_display = ('code', 'weight', 'css_class')
    list_editable = ('weight', 'css_class')
    
site.register(SitePosition, SitePositionAdmin)