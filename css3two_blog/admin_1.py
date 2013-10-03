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


    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.delete_old_md_file()
        return super(BlogPostModelAdmin, self).change_view(request, object_id,)   
    
    
    form = MyModelForm

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':100, 'cols':100})},
    }
    
    def save_model(self, request, obj, form, change):
        flag = 0
        if obj:
            if obj.body:    # body有内容的时候才会更新md_file
                flag = 1
                url = 'content/BlogPost/2013/README.md'
                new_md_file = ContentFile(obj.body.encode('utf-8'))
                obj.md_file.save(obj.filename, new_md_file) 
                obj.md_file.close()
        obj.save()



admin.site.register(BlogPost, BlogPostModelAdmin)
