from django.conf import settings

SLIDER_TEMPLATE_PATH = getattr(settings, 'SITE_SLIDER_SLIDER_TEMPLATE_PATH', 'site_slider/slider.html')
SLIDE_TEMPLATE_PATH = getattr(settings, 'SITE_SLIDER_SLIDE_TEMPLATE_PATH', 'site_slider/slide.html')
