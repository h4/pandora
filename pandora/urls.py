from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pandora.views.home', name='home'),
    # url(r'^pandora/', include('pandora.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'box.views.list'),
    url(r'^new/$', 'box.views.new_items'),
    url(r'^things/(?P<id>[0-9]+)/$', 'box.views.item'),
)
