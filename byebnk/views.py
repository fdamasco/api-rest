
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .models import Ativo, Resgate, Aplicacao, Saldo
from . import serializers
from .serializers import AtivoSerializer, AplicacaoSerializer, ResgateSerializer, SaldoSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class AtivoList(generics.ListCreateAPIView):
  queryset = Ativo.objects.all()
  serializer_class = AtivoSerializer
  authentication_classes = [BasicAuthentication, TokenAuthentication,]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
  
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
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request, format=None):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        return Response(content)
  
      

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer




