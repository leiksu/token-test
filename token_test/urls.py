from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^register_app/$' , 'token_api.views.register_app'),
    url(r'^store_data/(\w+)/(\w+)/(\w+)/$' , 'token_api.views.store_data'),
    url(r'^retrieve_data/(\w+)/(\w*)$' , 'token_api.views.retrieve_data'),
    url(r'^admin/', include(admin.site.urls)),
)
