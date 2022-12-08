from django.contrib import admin
from .models import Ativo, Aplicacao, Resgate


admin.site.register(Ativo)
admin.site.register(Aplicacao)
admin.site.register(Resgate)