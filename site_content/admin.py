from django.conf import settings
from django.contrib.admin import site, ModelAdmin, StackedInline, TabularInline
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from site_content.settings import ENABLE_BUILTIN_MEDIA, RTE_CONFIG_URI
from site_content.models import InheritanceQuerySet, SitePage, SitePageTemplateSelection, SiteMenu, SiteMenuItem, MenuItemLink, MenuItemPage, SiteBlock, SitePageAlias, SitePageRedirect, SitePosition, SitePagePositionBlock


class SitePageTemplateSelectionAdmin(ModelAdmin):
    list_filter = ('is_system',)
    list_display = ('label', 'description', 'template_path', 'is_system')

site.register(SitePageTemplateSelection, SitePageTemplateSelectionAdmin)


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
    fields = ('siteposition', 'siteblocks', 'weight')
    allow_add = True
    extra = 0


class SitePageAdmin(ModelAdmin):
    list_display = ('url', 'content_header', 'template', 'site')
    list_filter = ('site', )
    list_editable = ('template', )
    save_on_top = True
    inlines = (SitePageAliasInline, SitePageRedirectInline, SitePagePositionBlockInline)
    ordering = ('url', )

    fieldsets = (
        (None, {'fields': ('site', 'is_index', 'url', 'title', 'content_header', 'enable_rte', 'content')}),
        ('Meta Tags', {'classes': ('collapse closed',), 'fields': ('meta_description', 'meta_keywords')}),
        ('Advanced', {'classes': ('collapse closed',), 'fields': ('page_class', 'template', 'custom_template')})
    )

    if ENABLE_BUILTIN_MEDIA:
        class Media:
            css = {'all': ('site_content/css/grappelli-tinymce.css',)}
            js = (getattr(settings, 'STATIC_URL', '') + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', RTE_CONFIG_URI)

    def __unicode__(self):
        return '%s' % 'administration'

site.register(SitePage, SitePageAdmin)


def delete_menu_items(modeladmin, request, queryset):
    for item in queryset:
        item.delete()

delete_menu_items.short_description = "Delete Selected Menu Items"


class SiteMenuItemAdmin(ModelAdmin):
    list_display = ('edit_item', 'label', 'weight', 'url', 'page', 'sitemenu', 'submenu', 'css_class')
    list_editable = ('weight', )
    list_filter = ('sitemenu', )

    fieldsets = (
        (None, {'fields': ('label', 'sitemenu', 'weight')}),
        ('Advanced', {'classes': ('collapse closed', ), 'fields': ('css_class', 'submenu')}),
    )

    change_list_template = 'site_content/menuitem_change_list.html'
    change_form_template = 'site_content/menuitem_change_form.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['change_link_url'] = urlresolvers.reverse('admin:site_content_menuitemlink_add')
        extra_context['change_page_url'] = urlresolvers.reverse('admin:site_content_menuitempage_add')
        return super(SiteMenuItemAdmin, self).changelist_view(request, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(SiteMenuItemAdmin, self).add_view(request, form_url='', extra_context=extra_context)
        return result

    def change_view(self, request, object_id, extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(SiteMenuItemAdmin, self).change_view(request, object_id, extra_context=extra_context)
        return result

    def queryset(self, request):
        qs = InheritanceQuerySet(SiteMenuItem).select_subclasses()
        return qs

    def url(self, obj):
        if obj.url:
            return obj.url
        else:
            return None

    def page(self, obj):
        if obj.page:
            return obj.page
        else:
            return None

    def edit_item(self, obj):
        item_url = 'admin:site_content_sitemenuitem_change'
        try:
            if obj.url:
                item_url = 'admin:site_content_menuitemlink_change'
        except:
            pass
        try:
            if obj.page:
                item_url = 'admin:site_content_menuitempage_change'
        except:
            pass
        retval = u'<a href="{0}">Edit</a>'.format(urlresolvers.reverse(item_url, args=(obj.id, )))
        return retval

    edit_item.allow_tags = True

    actions = [delete_menu_items]

    def get_actions(self, request):
        actions = super(SiteMenuItemAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

site.register(SiteMenuItem, SiteMenuItemAdmin)


class MenuItemLinkAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('label', 'sitemenu', 'url', 'weight')}),
        ('Advanced', {'classes': ('collapse closed', ), 'fields': ('css_class', 'target', 'submenu')}),
    )

    change_form_template = 'site_content/menuitem_change_form.html'

    def get_model_perms(self, request):
        return {}

    def add_view(self, request, form_url='', extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(MenuItemLinkAdmin, self).add_view(request, form_url='', extra_context=extra_context)
        return result

    def change_view(self, request, object_id, extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(MenuItemLinkAdmin, self).change_view(request, object_id, extra_context=extra_context)
        return result

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and '_continue' not in request.POST:
            change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
            return HttpResponseRedirect(change_list_url)
        return super(MenuItemLinkAdmin, self).response_change(request, obj)

    def response_change(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and '_continue' not in request.POST:
            change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
            return HttpResponseRedirect(change_list_url)
        return super(MenuItemLinkAdmin, self).response_change(request, obj)

site.register(MenuItemLink, MenuItemLinkAdmin)


class MenuItemPageAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('label', 'sitemenu', 'page', 'weight')}),
        ('Advanced', {'classes': ('collapse closed', ), 'fields': ('css_class', 'target', 'submenu')}),
    )

    change_form_template = 'site_content/menuitem_change_form.html'

    def get_model_perms(self, request):
        return {}

    def add_view(self, request, form_url='', extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(MenuItemPageAdmin, self).add_view(request, form_url='', extra_context=extra_context)
        return result

    def change_view(self, request, object_id, extra_context=None):
        change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
        extra_context = extra_context or {}
        extra_context['change_list_url'] = change_list_url
        result = super(MenuItemPageAdmin, self).change_view(request, object_id, extra_context=extra_context)
        return result

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and '_continue' not in request.POST:
            change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
            return HttpResponseRedirect(change_list_url)
        return super(MenuItemPageAdmin, self).response_change(request, obj)

    def response_change(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and '_continue' not in request.POST:
            change_list_url = urlresolvers.reverse('admin:site_content_sitemenuitem_changelist')
            return HttpResponseRedirect(change_list_url)
        return super(MenuItemPageAdmin, self).response_change(request, obj)

site.register(MenuItemPage, MenuItemPageAdmin)


class SiteMenuAdmin(ModelAdmin):
    list_display = ('label', 'code', 'site', 'show_label')

    def __unicode__(self):
        return '%s' % 'administration'

site.register(SiteMenu, SiteMenuAdmin)


class SiteBlockAdmin(ModelAdmin):
    save_on_top = True
    list_display = ('code', 'css_class', 'siteposition', 'weight',)
    list_editable = ('css_class', 'siteposition', 'weight',)
    list_filter = ('siteposition',)

    class Media:
        css = {'all': ('site_content/css/grappelli-tinymce.css',)}
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
