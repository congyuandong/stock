from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('goods.urls')),
	url(r'^g/', include('goods.urls')),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)