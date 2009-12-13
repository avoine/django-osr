from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'osr.views.recording_list'),
    (r'^(.+)/$', 'osr.views.recording_detail'),
)
