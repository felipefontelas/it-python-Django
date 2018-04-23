from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.instituicao_list, name='instituicao_list'),
    url(r'^instituicao/(?P<pk>[0-9]+)/$', views.instituicao_detail, name='instituicao_detail'),
    url(r'^instituicao/new/$', views.instituicao_new, name='instituicao_new'),
    url(r'^instituicao/(?P<pk>\d+)/edit/$', views.instituicao_edit, name='instituicao_edit'),
    url(r'^instituicao/(?P<pk>\d+)/delete/$', views.instituicao_delete, name='instituicao_delete')
    
]