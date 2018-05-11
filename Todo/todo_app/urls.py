from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^todo/$', views.index, name='index'),
    url('hox/hossein', views.detail, name='detail'),
    url(r'^form/$', views.form, name='form'),
    url(r'^user_show/<int:item_test>', views.detail, name='show_user'),
]