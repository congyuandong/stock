from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name='Index'),
	)