
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import views
from rest_framework import permissions
from .models import Ativo, Resgate, Aplicacao
from . import serializers
from .serializers import AtivoSerializer, AplicacaoSerializer, ResgateSerializer, UserSerializer
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
  
  
class Saldo(views.APIView):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  

  def get(self, request, format=None):
           
        #mostrar saldo do prórprio usuário (adicionar módulo usuário)
        totalAplicacao = 0
            
        for obj in Aplicacao.objects.all():
          totalAplicacao = totalAplicacao + (obj.preco_unitario_a*obj.quantidade_ativos_a)
         
        totalResgate = 0  
        for obj in Resgate.objects.all():
          totalResgate = totalResgate + (obj.preco_unitario_r*obj.quantidade_ativos_r)

        saldo = float(totalAplicacao - totalResgate) 
        
        return Response ({"saldo": + saldo})
    
      
  
    

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer




