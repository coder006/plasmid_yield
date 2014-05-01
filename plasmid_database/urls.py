from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from views import *

urlpatterns = patterns('',
	url(r'^$', index, name = 'index'),
)