from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^todo/$', views.index, name='index'),
    url('hox/hossein', views.detail, name='detail'),
    url(r'^form/$', views.form, name='form'),
    url(r'^todo/user_show/', views.detail, name='show_user'),
    url(r'^search-form/', views.search_form, name='search'), 
]