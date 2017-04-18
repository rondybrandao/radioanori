'''
Created on 17 de abr de 2017

@author: rondy
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^pages/$', views.single_page, name='single_page'),
] 