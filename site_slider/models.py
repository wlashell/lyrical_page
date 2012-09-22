from django.db import models

from filebrowser.fields import FileBrowseField


class Slider(models.Model):
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    css_class = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True, help_text='Default template path is site_slider/slider.html')

    class Meta:
        ordering = ('label',)

    def __unicode__(self):
        return u'%s' % self.label


class SliderSlide(models.Model):
    slider = models.ForeignKey(Slider)
    weight = models.IntegerField(default=0)
    image = FileBrowseField(directory='slides', max_length=255, null=True, blank=True)
    image_css_class = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_css_class = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True, help_text='Default template path is site_slider/slide.html')

    class Meta:
        ordering = ('weight',)

    def __unicode__(self):
        return u'%s slide %s' % (self.slider.label, self.weight)
