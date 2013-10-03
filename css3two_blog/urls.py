from django.conf.urls import patterns,url
from css3two_blog import views

urlpatterns = patterns('',
    url('^$', views.home),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', views.blogpost),
    url('^tags/$', views.tags),
    url('^siteinfo/$', views.siteinfo),
    url('^contact/$', views.contact),
)
