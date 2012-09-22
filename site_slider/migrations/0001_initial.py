# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table('site_slider_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('css_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('site_slider', ['Slider'])

        # Adding model 'SliderSlide'
        db.create_table('site_slider_sliderslide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site_slider.Slider'])),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True, blank=True)),
            ('image_css_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_css_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('site_slider', ['SliderSlide'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table('site_slider_slider')

        # Deleting model 'SliderSlide'
        db.delete_table('site_slider_sliderslide')


    models = {
        'site_slider.slider': {
            'Meta': {'ordering': "('label',)", 'object_name': 'Slider'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'site_slider.sliderslide': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'SliderSlide'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_slider.Slider']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['site_slider']