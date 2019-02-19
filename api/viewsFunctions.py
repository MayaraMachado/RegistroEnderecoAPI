from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cliente.api.serializer import ClienteSerializer
from endereco.api.serializer import EnderecoSerializer
from cliente.models import Cliente

 @csrf_exempt
def todosClientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False )

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def especificoClientes(request, id=None):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(cliente, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cliente.delete() #Deletar logicamente
        return HttpResponse(status=204)


@csrf_exempt
def todosEnderecosClientes(request, id=None):
    cliente = Cliente.objects.get(id=id)

    if request.method == "GET":
        enderecos = cliente.endereco
        serializer = EnderecoSerializer(enderecos, many=True)
        return JsonResponse(serializer.data, safe=False )

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def especificoEnderecoClientes(request, id=None, idend=None):
    endereco = Cliente.objects.get(id=id).endereco.get(id=idend)

    if request.method == 'GET':
        serializer = EnderecoSerializer(endereco)
        if serializer:
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnderecoSerializer(endereco, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        endereco.delete() #Deletar logicamente
        return HttpResponse(status=204)

