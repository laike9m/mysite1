from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # css3two_blog:
    url(r'^$', 'css3two_blog.views.home'),
    url(r'^blog/', include('css3two_blog.urls')),
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include('article.urls')),
    
    #user auth urls
    url(r'^accounts/login/$', 'mysite1.views.login'),
    url(r'^accounts/auth/$', 'mysite1.views.auth_view'),
    url(r'^accounts/logout/$', 'mysite1.views.logout'),
    url(r'^accounts/loggedin/$', 'mysite1.views.loggedin'),
    url(r'^accounts/invalid/$', 'mysite1.views.invalid_login'),
    url(r'^accounts.register/$', 'mysite1.views.register_user'),
    url(r'^accounts.register_success/(?P<username>\w*)/$', 'mysite1.views.register_success')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
