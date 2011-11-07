from django import template

from site_tracking.models import VerificationCode, TRACK_GOOGLE_ANALYTICS

register = template.Library()

@register.inclusion_tag('site_tracking/meta_verify.html')
def st_meta_verification():
    return {'verifycodes': VerificationCode.objects.all()}

@register.inclusion_tag('site_tracking/js_google_analytics.html')
def st_ga_tracking():
    try:
        retval = TrackingCode.objects.get(tracking_code=TRACK_GOOGLE_ANALYTICS).code
    except TrackingCode.DoesNotExist:
        retval = ''
        
    return {'trackingcode': reval}