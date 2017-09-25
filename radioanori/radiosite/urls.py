'''
Created on 17 de abr de 2017

@author: rondy
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_comentario, name='post_comentario'),
    url(r'^loteria$', views.loteria, name='loteria'),
    url(r'^lotofacil/$', views.pesquisar_lotofacil, name='pesquisa'),
    url(r'^megasena$', views.pesquisar_megasena, name='pesquisa'),
    url(r'^megasena-result/$', views.pesquisar_megasena_result, name='pesquisa'),
    url(r'^anunciodoproduto/(?P<pk>[0-9]+)/$', views.anuncio, name='anuncio'),
    url(r'^anuncio-detalhe/(?P<pk>[0-9]+)$', views.post_anuncio, name='anuncio-detail'),
    url(r'^anuncio-detail/(?P<pk>[0-9]+)$', views.post_anuncio_detalhe, name='post_anuncio-detail'),
    url(r'^classificados$', views.ContactView.as_view(), name='post_classificados'),
    url(r'^form-classificado$', views.add_form, name='add_form'),
    url(r'^form_detail/(?P<pk>[0-9]+)/$', views.form_detail, name='form_detail'),
    url(r'^radiosite/mapas$', views.api_google_maps, name='api_google_maps'),
    url(r'^em_construcao$', views.em_construcao, name='em_construcao'),
    url(r'^anori$', views.anori, name='anori'),
    #url(r'^anunciar/$', views.anunciar, name='pesquisa'),
    #url(r'^pages/$', views.single_page, name='single_page'),
] 