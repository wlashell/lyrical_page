from django.contrib.admin import site, ModelAdmin, StackedInline

from site_content.settings import ENABLE_BUILTIN_MEDIA
from site_content.models import SitePage, SiteMenu, SiteMenuItem, SiteBlock, SitePageAlias, SitePageRedirect, SitePosition

site.register(SitePosition)

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

class SitePageAdmin(ModelAdmin):
    list_display = ('url', 'content_header', 'sitemenu', 'sitemenu_label', 'sitemenu_weight', 'template')
    list_filter = ('sitemenu',)
    list_editable = ('sitemenu', 'sitemenu_label', 'sitemenu_weight','template')
    save_on_top = True
    inlines = (SitePageAliasInline,SitePageRedirectInline)
    ordering = ('sitemenu', 'sitemenu_weight')
    
    fieldsets = (
        (None, {'fields': ('is_index', 'url', 'title', 'content_header', 'content')}),
        ('Menu', {'fields': ('sitemenu', 'sitemenu_label', 'sitemenu_weight')}),
        ('Meta Tags', {'classes': ('collapse closed',), 'fields': ('meta_description', 'meta_keywords')}),
        ('Advanced', {'classes': ('collapse closed',), 'fields': ('page_class', 'template')})
    )
    
    if ENABLE_BUILTIN_MEDIA:
        class Media:
            js = ('/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/js/lyrical_pageTinyMCEAdmin.js')
        
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
    class Media:
        js = ('/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/js/lyrical_pageTinyMCEAdmin.js')

    def __unicode__(self):
        return '%s' % 'administration'

site.register(SiteBlock, SiteBlockAdmin)

class SitePageRedirect(ModelAdmin):
    list_display = ('sitepage', 'url')
    save_on_top = True