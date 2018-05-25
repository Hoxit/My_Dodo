from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^todo/$', views.index, name='index'),
    url('hox/hossein', views.detail, name='detail'),
    url(r'^todo/user_show/', views.detail, name='show_user'),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
]