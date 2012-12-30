from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.fields.related import SingleRelatedObjectDescriptor
from django.db.models.query import QuerySet


class InheritanceQuerySet(QuerySet):
    def select_subclasses(self, *subclasses):
        if not subclasses:
            subclasses = [o for o in dir(self.model)
                          if isinstance(getattr(self.model, o), SingleRelatedObjectDescriptor)\
                          and issubclass(getattr(self.model, o).related.model, self.model)]
        new_qs = self.select_related(*subclasses)
        new_qs.subclasses = subclasses
        return new_qs

    def _clone(self, klass=None, setup=False, **kwargs):
        try:
            kwargs.update({'subclasses': self.subclasses})
        except AttributeError:
            pass
        return super(InheritanceQuerySet, self)._clone(klass, setup, **kwargs)

    def iterator(self):
        iqs_iter = super(InheritanceQuerySet, self).iterator()
        if getattr(self, 'subclasses', False):
            for obj in iqs_iter:
                obj = [getattr(obj, s) for s in self.subclasses if getattr(obj, s)] or [obj]
                yield obj[0]
        else:
            for obj in iqs_iter:
                yield obj


class SitePageTemplateSelection(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    template_path = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return u'%s' % self.label


class SitePage(models.Model):
    site = models.ForeignKey(Site)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    page_class = models.CharField(max_length=255, blank=True, null=True)
    content_header = models.CharField(max_length=255, blank=True, null=True)
    enable_rte = models.BooleanField(default=True, help_text='Check this box to use the graphical editor', verbose_name='Enable editor')
    content = models.TextField(blank=True, null=True)
    template = models.ForeignKey(SitePageTemplateSelection, blank=True, null=True)
    custom_template = models.CharField(max_length=255, blank=True, null=True, help_text='Enter a custom template path. This value will override the template selection dropdown.')
    is_index = models.BooleanField(blank=True, default=False)
    login_required = models.BooleanField(blank=True, default=False)

    class Meta:
        unique_together = ('site', 'url')

    def __unicode__(self):
        return u'%s' % (self.url)

    def save(self, force_insert=False, force_update=False):
        if self.is_index:
            for sitepage in SitePage.objects.filter(site=self.site):
                sitepage.is_index = False
                sitepage.save()

        if getattr(settings, 'APPEND_SLASH', False) and self.url != '/':
            if not self.url.startswith('/'):
                self.url = '/%s' % self.url
            if not self.url.endswith('/'):
                self.url = '%s/' % self.url

        super(SitePage, self).save(force_insert, force_update)


class SitePageAlias(models.Model):
    sitepage = models.ForeignKey(SitePage)
    url_alias = models.CharField(max_length=255,
                                 unique=True,
                                 help_text='Max character length for alias is 255.')

    def __unicode__(self):
        return u'%s' % self.url_alias


class SitePageRedirect(models.Model):
    sitepage = models.ForeignKey(SitePage)
    url = models.CharField(max_length=255,
                           unique=True,
                           help_text='URL to redirect. Max character length for alias is 255.')

    def __unicode__(self):
        return u'%s' % self.url


class SitePosition(models.Model):
    code = models.CharField(max_length=255, unique=True)
    weight = models.IntegerField(default=0)
    css_class = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.code


class SiteBlock(models.Model):
    siteposition = models.ForeignKey(SitePosition, blank=True, null=True)
    code = models.CharField(max_length=255, unique=True)
    css_class = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0, help_text='Blocks are displayed in descending order')
    enable_rte = models.BooleanField(default=True, help_text='Check this box to use the graphical editor', verbose_name='Enable editor')
    data = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.code)

    class Meta:
        ordering = ('weight',)


class SitePagePositionBlock(models.Model):
    sitepage = models.ForeignKey(SitePage)
    siteposition = models.ForeignKey(SitePosition)
    siteblocks = models.ForeignKey(SiteBlock)
    weight = models.IntegerField(default=0, help_text='Blocks are displayed in descending order')

    class Meta:
        ordering = ('weight',)


class SiteMenu(models.Model):
    site = models.ForeignKey(Site)
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    show_label = models.BooleanField(default=False)

    class Meta:
        unique_together = (['site', 'code'])

    def __unicode__(self):
        return u'{0}'.format(self.label)

    def get_menu_items(self):
        return InheritanceQuerySet(SiteMenuItem).filter(sitemenu=self).select_subclasses()


class SiteMenuItem(models.Model):
    sitemenu = models.ForeignKey(SiteMenu, related_name='sitemenu')
    label = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)
    css_class = models.CharField(max_length=255, blank=True)
    submenu = models.ForeignKey(SiteMenu, related_name='submenu', blank=True, null=True)

    class Meta:
        ordering = ['weight']

    def __unicode__(self):
        return u'{0}'.format(self.label)


class MenuItemLink(SiteMenuItem):
    url = models.CharField(max_length=255, blank=True)
    target = models.CharField(max_length=35, blank=True)


class MenuItemPage(SiteMenuItem):
    page = models.ForeignKey(SitePage)
    target = models.CharField(max_length=35, blank=True)
