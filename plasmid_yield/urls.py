from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plasmid_yield.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
if 'plasmid_database' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^plyield/', include('plasmid_database.urls')),
    )
