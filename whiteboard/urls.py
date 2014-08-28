from django.conf.urls import patterns, url
from whiteboard import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
