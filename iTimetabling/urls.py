from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.instituicao_list, name='instituicao_list'),
    url(r'^instituicao/(?P<pk>[0-9]+)/$', views.instituicao_detail, name='instituicao_detail'),
]