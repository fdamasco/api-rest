
from rest_framework import generics
from .models import Ativo, Resgate, Aplicacao
from .serializers import AtivoSerializer, AplicacaoSerializer, ResgateSerializer


class AtivoList(generics.ListCreateAPIView):
  queryset = Ativo.objects.all()
  serializer_class = AtivoSerializer


class AtivoDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Ativo.objects.all()
   serializer_class = AtivoSerializer



