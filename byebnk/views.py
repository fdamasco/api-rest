
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .models import Ativo, Resgate, Aplicacao
from .serializers import AtivoSerializer, AplicacaoSerializer, ResgateSerializer, UserSerializer


class AtivoList(generics.ListCreateAPIView):
  queryset = Ativo.objects.all()
  serializer_class = AtivoSerializer


class AtivoDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Ativo.objects.all()
   serializer_class = AtivoSerializer


class AplicacaoList(generics.ListCreateAPIView):
  queryset = Aplicacao.objects.all()
  serializer_class = AplicacaoSerializer


class ResgateList(generics.ListCreateAPIView):
  queryset = Resgate.objects.all()
  serializer_class = ResgateSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




