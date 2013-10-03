# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table('css3two_blog_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('md_file', self.gf('django.db.models.fields.files.FileField')(blank=True, max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 1, 0, 0))),
            ('last_edit_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 1, 0, 0))),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50)),
        ))
        db.send_create_signal('css3two_blog', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table('css3two_blog_blogpost')


    models = {
        'css3two_blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 1, 0, 0)'}),
            'md_file': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 1, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['css3two_blog']