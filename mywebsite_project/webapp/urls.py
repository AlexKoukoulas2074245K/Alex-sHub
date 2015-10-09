from django.conf.urls import patterns, url
from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_name_slug>[\w\-]+)/$', views.project, name='project'),
    )
