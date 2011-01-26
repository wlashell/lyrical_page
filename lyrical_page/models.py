from django.db import models


class SiteMenu(models.Model):
    label = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    weight = models.IntegerField()
    
    def __unicode__(self):
        return u'%s' % self.label

class SiteMenuItem(models.Model):
    sitemenu = models.ForeignKey(SiteMenu)
    label = models.CharField(max_length=255, unique=True)
    weight = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.label

class SitePage(models.Model):
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    page_class = models.CharField(max_length=255, blank=True, null=True)
    content_header = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)
    sitemenu = models.ForeignKey(SiteMenu, blank=True, null=True)
    sitemenu_label = models.CharField(max_length=255, blank=True, null=True)
    sitemenu_weight = models.IntegerField(blank=True, null=True)
    is_index = models.BooleanField(blank=True, default=False)
    
    def __unicode__(self):
        return u'%s' % (self.url)
    
    def save(self, force_insert=False, force_update=False):
        if self.is_index:
            for sitepage in SitePage.objects.all():
                sitepage.is_index = False
                sitepage.save()
                
        super(SitePage, self).save(force_insert, force_update)
    
class SiteBlock(models.Model):
    code = models.CharField(max_length=255, unique=True)
    data = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.code)
