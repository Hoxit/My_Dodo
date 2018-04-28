from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^todo/$', views.index, name='index'),
    url('hox/hossein', views.detail, name='detail'),
]