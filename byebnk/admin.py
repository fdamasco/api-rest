from django.contrib import admin
from .models import Ativo, Aplicacao, Resgate, Saldo


admin.site.register(Ativo)
admin.site.register(Aplicacao)
admin.site.register(Resgate)
admin.site.register(Saldo)