# -*- coding:utf-8 -*-
from django.contrib import admin
from css3two_blog.models import BlogPost

from django.forms import TextInput,Textarea
from django.db import models

from django import forms

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
from mysite1.settings import MEDIA_ROOT

class MyModelForm(forms.ModelForm):
    '在加载某篇文章的admin页面时从md_file读取内容到body'
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        if self.instance.md_file:
            self.initial['body'] = self.instance.md_file.read()


class BlogPostModelAdmin(admin.ModelAdmin):
    
    def delete_old_md_file(self):
        # 删除旧的md文件
        md_file_list = []
        for blogpost in BlogPost.objects.all():
            if blogpost.md_file:
                md_file_list.append(blogpost.filename)
        
        with open('md_file_list.txt', 'wt') as f:
            f.write(str(md_file_list))
        
        for root, subdirs, files in os.walk(os.path.join(MEDIA_ROOT, 'content/BlogPost')):
            for file in files:
                if file not in md_file_list:
                    os.remove(os.path.join(root, file))

    '''
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.delete_old_md_file()
        return super(BlogPostModelAdmin, self).change_view(request, object_id,)   
    '''

    form = MyModelForm

    formfield_overrides = {  # 修改body显示框的大小使能容纳整篇文章
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':100, 'cols':100})},
    }
    
    def save_model(self, request, obj, form, change):
        if obj:
            if obj.body:    # body有内容的时候才会更新md_file
                new_md_file = ContentFile(obj.body.encode('utf-8'))
                filename = obj.filename
                #if filename == 'no md_file':
                    #filename = obj.title + '.md'    # 没有md_file就根据title创建一个
                #else:
                    #obj.md_file.delete()   # 这句在部署的时候存在,可以正常删除文件
                obj.md_file.save(filename, new_md_file)
                obj.md_file.close()
        obj.save()

        

admin.site.register(BlogPost, BlogPostModelAdmin)
