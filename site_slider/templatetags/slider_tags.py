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

        idx = 0
        for slide in slider.sliderslide_set.all().order_by('weight'):
            if slide.template:
                tmpl_path = slide.template
            else:
                tmpl_path = SLIDE_TEMPLATE_PATH

            tmpl = get_template(tmpl_path)
            retval += tmpl.render(Context({'slide': slide,
                                           'idx': idx}))
            idx += 1

        return retval


@register.tag
def get_slider(parser, token):
    tag_name, code = token.split_contents()

    return SliderNode(code)
