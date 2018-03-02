from django.urls import path, re_path

from . import views

urlpatterns = [
    # /data/
    path('', views.index, name='index'),
    # /data/35/
    re_path(r'^(?P<sample_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<sample_id>[0-9]+)/$', views.table, name='table'),
]
