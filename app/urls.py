from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import  include, path
from rest_framework import routers, serializers, viewsets, permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('byebnk/', include('byebnk.urls'))
]