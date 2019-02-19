from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro','bairro', 'cidade', 'estado', 'numero', 'principal' )
