from rest_framework import serializers
from .models import *

class LocaisDescarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocaisDescarte
        fields = ['id', 'nome_local', 'rua', 'bairro', 'cidade', 'estado', 'celular', 'email', 'site']
