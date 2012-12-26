# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SitePage.template'
        db.delete_column('site_content_sitepage', 'template')

        # Adding field 'SitePage.custom_template'
        db.add_column('site_content_sitepage', 'custom_template',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SitePage.template'
        db.add_column('site_content_sitepage', 'template',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SitePage.custom_template'
        db.delete_column('site_content_sitepage', 'custom_template')


    models = {
        'site_content.menuitemlink': {
            'Meta': {'ordering': "['weight']", 'object_name': 'MenuItemLink', '_ormbases': ['site_content.SiteMenuItem']},
            'sitemenuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['site_content.SiteMenuItem']", 'unique': 'True', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'site_content.menuitempage': {
            'Meta': {'ordering': "['weight']", 'object_name': 'MenuItemPage', '_ormbases': ['site_content.SiteMenuItem']},
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'sitemenuitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['site_content.SiteMenuItem']", 'unique': 'True', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'site_content.siteblock': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'SiteBlock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_rte': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteposition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePosition']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'site_content.sitemenu': {
            'Meta': {'unique_together': "(['site', 'code'],)", 'object_name': 'SiteMenu'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_label': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'site_content.sitemenuitem': {
            'Meta': {'ordering': "['weight']", 'object_name': 'SiteMenuItem'},
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sitemenu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sitemenu'", 'to': "orm['site_content.SiteMenu']"}),
            'submenu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'submenu'", 'null': 'True', 'to': "orm['site_content.SiteMenu']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'site_content.sitepage': {
            'Meta': {'unique_together': "(('site', 'url'),)", 'object_name': 'SitePage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'custom_template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'enable_rte': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'page_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'site_content.sitepagealias': {
            'Meta': {'object_name': 'SitePageAlias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url_alias': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.sitepagepositionblock': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'SitePagePositionBlock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteblocks': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteBlock']"}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'siteposition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePosition']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'site_content.sitepageredirect': {
            'Meta': {'object_name': 'SitePageRedirect'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.sitepagetemplateselection': {
            'Meta': {'object_name': 'SitePageTemplateSelection'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'template_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'site_content.siteposition': {
            'Meta': {'object_name': 'SitePosition'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['site_content']