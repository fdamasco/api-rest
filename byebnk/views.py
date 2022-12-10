
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .models import Ativo, Resgate, Aplicacao, Saldo
from . import serializers
from .serializers import AtivoSerializer, AplicacaoSerializer, ResgateSerializer, SaldoSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class AtivoList(generics.ListCreateAPIView):
  queryset = Ativo.objects.all()
  serializer_class = AtivoSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class AtivoDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Ativo.objects.all()
   serializer_class = AtivoSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


class AplicacaoList(generics.ListCreateAPIView):
  queryset = Aplicacao.objects.all()
  serializer_class = AplicacaoSerializer


class ResgateList(generics.ListCreateAPIView):
  queryset = Resgate.objects.all()
  serializer_class = ResgateSerializer
  
class SaldoList(generics.ListAPIView):
  queryset = Saldo.objects.all()
  serializer_class = SaldoSerializer

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer




