# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'SiteMenu'
        db.create_table('site_content_sitemenu', (
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('site_content', ['SiteMenu'])

        # Adding model 'SiteMenuItem'
        db.create_table('site_content_sitemenuitem', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sitemenu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SiteMenu'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('site_content', ['SiteMenuItem'])

        # Adding model 'SitePage'
        db.create_table('site_content_sitepage', (
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sitemenu_weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('content_header', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sitemenu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SiteMenu'], null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_index', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('login_required', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('page_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sitemenu_label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('site_content', ['SitePage'])

        # Adding model 'SitePageAlias'
        db.create_table('site_content_sitepagealias', (
            ('sitepage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SitePage'])),
            ('url_alias', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('site_content', ['SitePageAlias'])

        # Adding model 'SitePageRedirect'
        db.create_table('site_content_sitepageredirect', (
            ('sitepage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SitePage'])),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('site_content', ['SitePageRedirect'])

        # Adding model 'SiteBlock'
        db.create_table('site_content_siteblock', (
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('site_content', ['SiteBlock'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'SiteMenu'
        db.delete_table('site_content_sitemenu')

        # Deleting model 'SiteMenuItem'
        db.delete_table('site_content_sitemenuitem')

        # Deleting model 'SitePage'
        db.delete_table('site_content_sitepage')

        # Deleting model 'SitePageAlias'
        db.delete_table('site_content_sitepagealias')

        # Deleting model 'SitePageRedirect'
        db.delete_table('site_content_sitepageredirect')

        # Deleting model 'SiteBlock'
        db.delete_table('site_content_siteblock')
    
    
    models = {
        'site_content.siteblock': {
            'Meta': {'object_name': 'SiteBlock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'site_content.sitemenu': {
            'Meta': {'object_name': 'SiteMenu'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'site_content.sitemenuitem': {
            'Meta': {'object_name': 'SiteMenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'sitemenu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteMenu']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'site_content.sitepage': {
            'Meta': {'object_name': 'SitePage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'page_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sitemenu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteMenu']", 'null': 'True', 'blank': 'True'}),
            'sitemenu_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sitemenu_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.sitepagealias': {
            'Meta': {'object_name': 'SitePageAlias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url_alias': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.sitepageredirect': {
            'Meta': {'object_name': 'SitePageRedirect'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }
    
    complete_apps = ['site_content']
