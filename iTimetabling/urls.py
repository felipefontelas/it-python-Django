from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.instituicao_list, name='instituicao_list')
]