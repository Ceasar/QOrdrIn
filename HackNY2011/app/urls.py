from django.conf.urls.defaults import patterns, include, url

from views import *

urlpatterns = patterns('',
    (r'^order/', order),
<<<<<<< HEAD
    (r'^thanks/', thanks),
    (r'^options/', options),
=======
>>>>>>> b53c11c2961795eb80760d1ec8e6236c93a35bb6
    (r'^menu/', menu),
    (r'^creditcard/', creditcard),
    (r'^', index),
    # Examples:
    # url(r'^$', 'hackny.views.home', name='home'),
    # url(r'^hackny/', include('hackny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
