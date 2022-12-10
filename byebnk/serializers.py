from django.contrib.auth.models import User
from .models import Ativo, Resgate, Aplicacao, Saldo
from rest_framework import serializers


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

class UserSerializer(serializers.ModelSerializer):
    ativo = serializers.PrimaryKeyRelatedField(many=True, queryset=Ativo.objects.all())
    class Meta:
        model = User
        fields = ('__all__')

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
      model = Saldo
      fields = ('__all__')



