from django.contrib.admin import site, ModelAdmin

from site_tracking.models import VerificationCode, TrackingCode

class VerificationCodeAdmin(ModelAdmin):
    list_display = ('site', 'verification_type', 'code',)
    list_editable = ('code',)
    
site.register(VerificationCode, VerificationCodeAdmin)

class TrackingCodeAdmin(ModelAdmin):
    list_display = ('site', 'tracking_type', 'code')
    list_editable = ('tracking_type', 'code')
    
site.register(TrackingCode, TrackingCodeAdmin)