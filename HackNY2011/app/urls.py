from django.conf.urls.defaults import patterns, include, url

from views import *

urlpatterns = patterns('',
    (r'^order/', order),
    (r'^thanks/', thanks),
    (r'^menu/', menu),
    (r'^creditcard/', creditcard),
    (r'^success/', success),
    (r'^', index),
    # Examples:
    # url(r'^$', 'hackny.views.home', name='home'),
    # url(r'^hackny/', include('hackny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
