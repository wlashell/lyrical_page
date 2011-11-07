from django.contrib.admin import site, ModelAdmin

from site_tracking.models import VerificationCode

class VerificationCodeAdmin(ModelAdmin):
    list_display = ('site', 'verification_type', 'code',)
    list_editable = ('code',)
    
site.register(VerficationCode, VerificationCodeAdmin)