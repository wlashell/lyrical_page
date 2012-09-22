from django.conf import settings
from django.contrib.admin import site, ModelAdmin

from site_content.settings import RTE_CONFIG_URI

from site_slider.models import Slider, SliderSlide


class SliderAdmin(ModelAdmin):
    list_display = ('label', 'code', 'css_class')
    list_editable = ('code', 'css_class')

site.register(Slider, SliderAdmin)


class SliderSlideAdmin(ModelAdmin):
    list_display = ('get_admin_label', 'slider', 'weight')
    list_editable = ('weight',)
    change_form_template = 'admin/site_content/change_form.html'

    class Media:
        css = {'all': ('site_content/css/grappelli-tinymce.css',)}
        js = (getattr(settings, 'STATIC_URL', '') + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', RTE_CONFIG_URI)

    def get_admin_label(self, obj):
        return u'%s - %s' % (obj.slider.label, obj.weight)

site.register(SliderSlide, SliderSlideAdmin)
