from django.contrib.auth.models import User
from .models import Ativo, Resgate, Aplicacao
from rest_framework import serializers


class AtivoSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = User
        fields = ('__all__')



