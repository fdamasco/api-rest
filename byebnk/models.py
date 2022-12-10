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
  valor = models.DecimalField(max_digits=12, decimal_places=2)

  class Meta:
      verbose_name_plural = "aplicações"
  

class Resgate(models.Model):
  
  ativo = models.ForeignKey(
     Ativo,
    models.SET_NULL,
    blank=True,
    null=True,)
  valor = models.DecimalField(max_digits=12, decimal_places=2)
  
class Saldo(models.Model):
  saldo = models.DecimalField(max_digits=12, decimal_places=2)




