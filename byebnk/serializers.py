from django.contrib.auth.models import User
from .models import Ativo, Resgate, Aplicacao
from rest_framework import serializers
from . import views


class AtivoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
      model = Ativo
      fields = ('__all__')


class AplicacaoSerializer(serializers.ModelSerializer):
    class Meta:
      model = Aplicacao
      fields = ('__all__')

class ResgateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Resgate
      fields = ('__all__')
      
    def validate(self, resgate):
      
      totalAplicacao = 0
      for obj in Aplicacao.objects.all():
          totalAplicacao = totalAplicacao + (obj.preco_unitario_a*obj.quantidade_ativos_a)
         
      totalResgate = 0  
      for obj in Resgate.objects.all():
          totalResgate = totalResgate + (obj.preco_unitario_r*obj.quantidade_ativos_r)

      saldo = totalAplicacao - totalResgate 
      
      
      if Aplicacao.objects.all == 0:
          raise serializers.ValidationError("Você não possui saldo para resgate.")
      elif saldo <= 0:
          raise serializers.ValidationError("Você não possui saldo para resgate.")
      elif obj.preco_unitario_r*obj.quantidade_ativos_r > saldo:
        raise serializers.ValidationError("Você não possui este saldo para resgate.")        
      return resgate
      

class UserSerializer(serializers.ModelSerializer):
    ativo = serializers.PrimaryKeyRelatedField(many=True, queryset=Ativo.objects.all())
    class Meta:
        model = User
        fields = ('__all__')



