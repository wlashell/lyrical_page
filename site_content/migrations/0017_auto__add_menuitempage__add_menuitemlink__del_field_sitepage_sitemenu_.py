# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SiteMenu', fields ['label']
        db.delete_unique('site_content_sitemenu', ['label'])

        # Removing unique constraint on 'SiteMenu', fields ['code']
        db.delete_unique('site_content_sitemenu', ['code'])

        # Removing unique constraint on 'SiteMenuItem', fields ['label']
        db.delete_unique('site_content_sitemenuitem', ['label'])

        # Adding model 'MenuItemPage'
        db.create_table('site_content_menuitempage', (
            ('sitemenuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['site_content.SiteMenuItem'], unique=True, primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SitePage'])),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('site_content', ['MenuItemPage'])

        # Adding model 'MenuItemLink'
        db.create_table('site_content_menuitemlink', (
            ('sitemenuitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['site_content.SiteMenuItem'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('site_content', ['MenuItemLink'])

        # Deleting field 'SitePage.sitemenu_label'
        db.delete_column('site_content_sitepage', 'sitemenu_label')

        # Deleting field 'SitePage.sitemenu'
        db.delete_column('site_content_sitepage', 'sitemenu_id')

        # Deleting field 'SitePage.sitemenu_css_class'
        db.delete_column('site_content_sitepage', 'sitemenu_css_class')

        # Deleting field 'SitePage.sitemenu_depth'
        db.delete_column('site_content_sitepage', 'sitemenu_depth')

        # Deleting field 'SitePage.sitemenu_weight'
        db.delete_column('site_content_sitepage', 'sitemenu_weight')

        # Deleting field 'SiteMenuItem.url'
        db.delete_column('site_content_sitemenuitem', 'url')

        # Adding field 'SiteMenuItem.submenu'
        db.add_column('site_content_sitemenuitem', 'submenu',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='submenu', null=True, to=orm['site_content.SiteMenu']),
                      keep_default=False)


        # Changing field 'SiteMenuItem.css_class'
        db.alter_column('site_content_sitemenuitem', 'css_class', self.gf('django.db.models.fields.CharField')(default='', max_length=255))
        # Deleting field 'SiteMenu.weight'
        db.delete_column('site_content_sitemenu', 'weight')

        # Adding field 'SiteMenu.site'
        db.add_column('site_content_sitemenu', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'SiteMenu.show_label'
        db.add_column('site_content_sitemenu', 'show_label',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding unique constraint on 'SiteMenu', fields ['code', 'site']
        db.create_unique('site_content_sitemenu', ['code', 'site_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'SiteMenu', fields ['code', 'site']
        db.delete_unique('site_content_sitemenu', ['code', 'site_id'])

        # Deleting model 'MenuItemPage'
        db.delete_table('site_content_menuitempage')

        # Deleting model 'MenuItemLink'
        db.delete_table('site_content_menuitemlink')

        # Adding field 'SitePage.sitemenu_label'
        db.add_column('site_content_sitepage', 'sitemenu_label',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SitePage.sitemenu'
        db.add_column('site_content_sitepage', 'sitemenu',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_content.SiteMenu'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'SitePage.sitemenu_css_class'
        db.add_column('site_content_sitepage', 'sitemenu_css_class',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SitePage.sitemenu_depth'
        db.add_column('site_content_sitepage', 'sitemenu_depth',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SitePage.sitemenu_weight'
        db.add_column('site_content_sitepage', 'sitemenu_weight',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteMenuItem.url'
        db.add_column('site_content_sitemenuitem', 'url',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SiteMenuItem.submenu'
        db.delete_column('site_content_sitemenuitem', 'submenu_id')


        # Changing field 'SiteMenuItem.css_class'
        db.alter_column('site_content_sitemenuitem', 'css_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding unique constraint on 'SiteMenuItem', fields ['label']
        db.create_unique('site_content_sitemenuitem', ['label'])

        # Adding field 'SiteMenu.weight'
        db.add_column('site_content_sitemenu', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'SiteMenu.site'
        db.delete_column('site_content_sitemenu', 'site_id')

        # Deleting field 'SiteMenu.show_label'
        db.delete_column('site_content_sitemenu', 'show_label')

        # Adding unique constraint on 'SiteMenu', fields ['code']
        db.create_unique('site_content_sitemenu', ['code'])

        # Adding unique constraint on 'SiteMenu', fields ['label']
        db.create_unique('site_content_sitemenu', ['label'])

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
            'enable_rte': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'page_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
