import datetime

from django.contrib.sites.models import Site
from django.db import models

from site_content.models import SitePage


class SiteUrl(models.Model):
    site = models.ForeignKey(Site)
    sitepages = models.ManyToManyField(SitePage, blank=True, null=True)
    url = models.CharField(max_length=255, blank=False)
    page_title = models.TextField(blank=True, null=True)
    page_keywords = models.TextField(blank=True, null=True)
    page_description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(SiteUrl, self).save(*args, **kwargs)

        sitepages = SitePage.objects.filter(url=self.url, site=self.site)
        for sitepage in sitepages:
            self.sitepages.add(sitepage)


class SiteUrlDefaults(models.Model):
    site = models.ForeignKey(Site)
    page_title = models.TextField(blank=True, null=True)
    page_keywords = models.TextField(blank=True, null=True)
    page_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'site url defaults'

    def __unicode__(self):
        return 'SEO Default for site: %s' % self.site


class SiteUrl404(models.Model):
    site = models.ForeignKey(Site)
    url = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    date_list_hit = models.DateTimeField(default=datetime.datetime.now, auto_now=True)
    hit_cnt = models.IntegerField(default=0)

    class Meta:
        ordering = ('url',)
