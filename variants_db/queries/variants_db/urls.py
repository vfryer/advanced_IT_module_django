from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('queries/', include('queries.urls')),
    path('data/', include('data.urls')),
    path('admin/', admin.site.urls),
]
