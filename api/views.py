from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cliente.api.serializer import ClienteSerializer
from endereco.api.serializer import EnderecoSerializer
from cliente.models import Cliente
from endereco.models import Endereco

#Mixins
from rest_framework import mixins
from rest_framework import generics


##########
#GET, POST
class TodosClientes(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


##########
#GET, PUT, PATCH, DELETE
class EspecificoClientes(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)
        return self.patch(request, *args, **kwargs)




##########
#GET, POST(adicionar ao cliente)
class TodosEnderecosClientes(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    serializer_class = EnderecoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        return obj

    def get_queryset(self):
        id = self.kwargs['id']
        return Cliente.objects.get(id=id).endereco

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        end = self.create(request, *args, **kwargs)
        data = end.data
        serializer = EnderecoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            cliente = self.get_object()
            data['idCliente'] = self.get_object().id
            serializerCliente = ClienteSerializer(cliente, data=data)
            if serializerCliente.is_valid():
                serializerCliente.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse(serializer.errors, status=400)





##########
#GET, PUT, PATCH, DELETE
class EspecificoEnderecoClientes(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    serializer_class = EnderecoSerializer
    lookup_field = 'id'


    def get_queryset(self):
        id = self.kwargs['id']
        cliente = Cliente.objects.get(id=id)
        return cliente

    def get_object(self):
        idend = self.kwargs['idend']
        cliente = self.get_queryset()
        return cliente.endereco.get(id=idend)
        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)
        return self.partial_update(request, *args, **kwargs)



