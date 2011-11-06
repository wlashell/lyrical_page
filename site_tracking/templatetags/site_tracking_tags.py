from django import template

from site_tracking import VerificationCode

register = template.Library()

@register.inclusion_tag('meta_verify.html')
def st_meta_verification():
    return {'verifycodes': VerficationCode.objects.all()}