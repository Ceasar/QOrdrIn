from django.conf.urls.defaults import patterns, include, url

from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^order/', order),
    (r'^menu/', menu),
    (r'login/$', login),
    (r'create/$', create),
    (r'^', index),
    # Examples:
    # url(r'^$', 'hackny.views.home', name='home'),
    # url(r'^hackny/', include('hackny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
