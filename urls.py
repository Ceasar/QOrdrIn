from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from app import urls

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include(urls)),
    # Examples:
    # url(r'^$', 'hackny.views.home', name='home'),
    # url(r'^hackny/', include('hackny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
