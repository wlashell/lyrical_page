from django import template

from site_tracking.models import VerificationCode

register = template.Library()

@register.inclusion_tag('site_tracking/meta_verify.html')
def st_meta_verification():
    return {'verifycodes': VerificationCode.objects.all()}