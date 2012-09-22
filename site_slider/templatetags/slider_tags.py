from django.template import Library, Node, Context
from django.template.loader import render_to_string, get_template

from site_slider.models import Slider
from site_slider.settings import SLIDER_TEMPLATE_PATH, SLIDE_TEMPLATE_PATH

register = Library()


class SliderNode(Node):
    def __init__(self, code):
        self.code = code

    def render(self, context):
        slider = Slider.objects.get(code=self.code)
        retval = ''
        slides_html = ''

        idx = 0
        for slide in slider.sliderslide_set.all().order_by('weight'):
            if slide.template:
                tmpl_path = slide.template
            else:
                tmpl_path = SLIDE_TEMPLATE_PATH

            tmpl = get_template(tmpl_path)
            slides_html += tmpl.render(Context({'slide': slide,
                                           'idx': idx}))
            idx += 1

        if slider.template:
            tmpl_path = slider.template
        else:
            tmpl_path = SLIDER_TEMPLATE_PATH

        tmpl = get_template(tmpl_path)

        retval = tmpl.render(Context({'slider': slider,
                                      'slides_html': slides_html}))

        return retval


@register.tag
def get_slider(parser, token):
    tag_name, code = token.split_contents()

    return SliderNode(code)

