from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'example.core.views.home', name='home'),
)
