from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    
    fields = ['pub_date', 'question']
    '''
    fieldsets = [
                 ('Date',{'fields':['pub_date']}),
                 (None,{'fields':['question'],'classes':['collapse']}),
                 ]
    '''
    inlines = [ChoiceInline]
    list_display = ('question','pub_date','was_published_recently')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    
    
admin.site.register(Poll, PollAdmin)#����Ա�����Ķ�����admin.py���涨��.��Ҫ��models��������.