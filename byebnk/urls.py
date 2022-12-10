from django.urls import include, path
from rest_framework import viewsets
from . import views
from .views import AplicacaoList, AtivoList, AtivoDetail, ResgateList, UserList
from rest_framework import routers


urlpatterns = [
   path('ativo/', AtivoList.as_view()),
   path('ativo/<int:pk>', AtivoDetail.as_view()),
   path('users/', views.UserList.as_view()),
   path('aplicacao/', views.AplicacaoList.as_view()),
   path('resgate/', views.ResgateList.as_view()),
]

