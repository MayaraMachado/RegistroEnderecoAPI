from rest_framework.serializers import ModelSerializer
from cliente.models import Cliente
from endereco.models import Endereco
from endereco.api.serializer import EnderecoSerializer
from django.shortcuts import get_object_or_404

class ClienteSerializer(ModelSerializer):
    endereco = EnderecoSerializer(many=True, partial=True)

    class Meta:
        model = Cliente
        fields = ['id','foto', 'nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email', 'endereco']


    def criar_enderecos(self, enderecos, cliente):
        for endereco in enderecos:
            cliente_novo_endereco = Endereco.objects.get(logradouro=endereco['logradouro'],bairro= endereco['bairro'],cidade=endereco['cidade'],estado=endereco['estado'], numero=endereco['numero'])
            if not cliente_novo_endereco:
                cliente_novo_endereco = Endereco.objects.save(**endereco) 
            cliente.endereco.add(cliente_novo_endereco)
        return cliente 

    def create(self, id,  validated_data):
        enderecos = validated_data['endereco']
        del validated_data['endereco']

        cliente = Cliente.objects.get_or_create(id=id, defaults=validated_data)
        cliente = self.criar_enderecos(enderecos, cliente)

        cliente.save()
        return cliente


    def update(self, instance, validated_data):
        idCliente = validated_data.pop('idCliente')

        cliente = Cliente.objects.get(id=idCliente)
        cliente = self.criar_enderecos(validated_data, cliente)

        cliente.save()
        return cliente

    
    

 

