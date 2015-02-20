from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'simple.views.render_p1'),
    url(r'^short/', 'simple.views.render_p2'),
)
