from django.db import models
import datetime


class Ativo(models.Model):
   nome = models.CharField(max_length=100)
   modalidade = models.CharField(max_length=200)
   owner = models.ForeignKey(
     'auth.User',
     related_name='ativo',
     on_delete=models.CASCADE)


   def __str__(self):
    return self.nome


class Aplicacao(models.Model):
  
  ativo = models.ForeignKey(
    Ativo,
    models.SET_NULL,
    blank=True,
    null=True,)
  data_solicitacao = models.DateField()
  preco_unitario_a = models.DecimalField(max_digits=12, decimal_places=2)
  quantidade_ativos_a = models.IntegerField()
  

  class Meta:
      verbose_name_plural = "aplicações"
  

class Resgate(models.Model):
  
  ativo = models.ForeignKey(
     Ativo,
    models.SET_NULL,
    blank=True,
    null=True,)
  data_solicitacao = models.DateField
  preco_unitario_r = models.DecimalField(max_digits=12, decimal_places=2)
  quantidade_ativos_r = models.IntegerField()


  



