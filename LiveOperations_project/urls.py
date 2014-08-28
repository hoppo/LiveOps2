from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from LiveOperations_project.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LiveOperations_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^IMGGaming/', include('IMGGaming.urls')),
    url(r'^whiteboard/', include('whiteboard.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), 
)
