from django.db import models
from django.contrib.sites.models import Site

VERIFY_GOOGLE_WEBMASTER = 0
VERIFY_BING_WEBMASTER = 1
VERIFY_YAHOO_SITE_EXPLORER = 2

VERIFY_CHOICES = ((VERIFY_GOOGLE_WEBMASTER, 'Google Webmaster Tools'),
                    (VERIFY_BING_WEBMASTER, 'Bing Webmaster Tools'),
                    (VERIFY_YAHOO_SITE_EXPLORER, 'Yahoo Site Explorer'))

TRACK_GOOGLE_ANALYTICS = 0

TRACKING_CHOICES = ((TRACK_GOOGLE_ANALYTICS, 'Google Analytics'),)

class VerificationCode(models.Model):
    site = models.ForeignKey(Site)
    verification_type = models.IntegerField(choices=VERIFY_CHOICES)
    code = models.CharField(max_length=255, blank=False)
    
    def as_meta(self):
        retval = ''
        if self.verification_type == VERIFY_GOOGLE_WEBMASTER:
            retval = '<meta name="google-site-verification" content="%s" />' % self.code
        elif self.verification_type == VERIFY_BING_WEBMASTER:
            retval = '<meta name="msvalidate.01" content="%s" />' % self.code
        elif self.verification_type == VERIFY_YAHOO_SITE_EXPLORER:
            retval = '<meta name="y_key" content="%s">' % self.code
            
        return retval
    
class TrackingCode(models.Model):
    site = models.ForeignKey(Site)
    tracking_type = models.IntegerField(choices=TRACKING_CHOICES)
    code = models.CharField(max_length=255, blank=False)
    
#  <meta name="google-site-verification" content="JbB2P26ZeGLJMR1W_Jic2j75ynE_dRGvo8SW_z6Jp5o" />
#  <META name="y_key" content="599117acbce33">
#  <meta name="msvalidate.01" content="1D5E53138AE39C22710D095F0B411845" />

# bing xml
#<?xml version="1.0"?>
#<users>
#        <user>1D5E53138AE39C22710D095F0B411845</user>
#</users>

#  google-site-verification: google4dfada3ea19f921b.html
