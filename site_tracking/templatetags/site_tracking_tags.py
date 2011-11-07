from django import template

from site_tracking.models import VerificationCode, TrackingCode, TRACK_GOOGLE_ANALYTICS

register = template.Library()

@register.inclusion_tag('site_tracking/meta_verify.html')
def st_meta_verification():
    return {'verifycodes': VerificationCode.objects.all()}

@register.inclusion_tag('site_tracking/js_google_analytics.html')
def st_ga_tracking():
    try:
        retval = TrackingCode.objects.get(tracking_type=TRACK_GOOGLE_ANALYTICS).code
    except TrackingCode.DoesNotExist:
        retval = ''
        
    return {'trackingcode': retval}