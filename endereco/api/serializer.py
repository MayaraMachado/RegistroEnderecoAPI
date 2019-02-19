from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco

class EnderecoSerializer(ModelSerializer):

    class Meta:
        model = Endereco
        fields = ['id','logradouro', 'bairro', 'cidade', 'estado', 'numero', 'principal', 'ativo']

def create(self, validated_data):
    return Endereco.objects.save(**validated_data)