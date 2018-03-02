from django.urls import path, re_path

from . import views

urlpatterns = [
    # /table/
    path('', views.table, name='table'),
    #re_path(r'^(?P<cdna_variant>[0-9]+)/$', views.table, name='table'),
]
