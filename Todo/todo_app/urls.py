from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from . import views
app_name = "todo_app"

urlpatterns = [
    # url(r'^todo/$', views.index, name='index'),
    # url(r'^<int:pk>$', views.detail, name='detail'),
    # url(r'^todo/user_show/', views.detail.as_view(), name='show_user'),
    # url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url('new', views.WorkCreate.as_view(), name='work_new'),
    url(r'^$', views.WorkList.as_view(), name='work_list'),
    url('view/(?P<pk>\d+)/$', views.WorkView.as_view(), name='work_view'),
    # url('ccs/(?P<pk>\d+)/$', views.WorkView.as_view(), name='works_view'),
    url('edit/(?P<pk>\d+)/$', views.WorkUpdate.as_view(), name='work_edit'),
    url('delete/(?P<pk>\d+)/$', views.WorkDelete.as_view(),
        name='work_delete'),
    # url('hox/hossein', views.detail, name='detail'),
    # url(r'^todo/user_show/', views.detail, name='show_user'),
]