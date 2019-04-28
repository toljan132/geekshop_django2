from django.conf.urls import url

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    url('^$', mainapp.products, name='index'),
    url(r'^(?P<pk>\d+)/$', mainapp.product, name='product'),
    url(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
]
