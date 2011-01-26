from django.contrib.admin import site, ModelAdmin, StackedInline

from lyrical_page.models import SitePage, SiteMenu, SiteMenuItem, SiteBlock

class SitePageAdmin(ModelAdmin):
    list_display = ('url', 'content_header', 'sitemenu', 'sitemenu_label')
    list_filter = ('sitemenu',)
    save_on_top = True
    
    fieldsets = (
        (None, {'fields': ('is_index', 'url', 'title', 'content_header', 'content')}),
        ('Menu', {'fields': ('sitemenu', 'sitemenu_label', 'sitemenu_weight')}),
        ('Meta Tags', {'classes': ('collapse',), 'fields': ('meta_description', 'meta_keywords')}),
        ('Advanced', {'classes': ('collapse',), 'fields': ('page_class', 'template')})
    )
    
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/lyrical_pageTinyMCEAdmin.js')
        
site.register(SitePage, SitePageAdmin)

class SiteMenuItemAdmin(ModelAdmin):
    list_display = ('label', 'weight', 'url', 'sitemenu')
    list_filter = ('sitemenu',)
    list_editable = ('weight',)
    ordering = ('weight',)

site.register(SiteMenuItem, SiteMenuItemAdmin)
site.register(SiteMenu)

class SiteBlockAdmin(ModelAdmin):
    save_on_top = True
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/lyrical_pageTinyMCEAdmin.js')
        
site.register(SiteBlock, SiteBlockAdmin)
