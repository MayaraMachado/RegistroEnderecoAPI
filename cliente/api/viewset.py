from rest_framework.viewsets import ModelViewSet
from .serializer import ClienteSerializer
from cliente.models import Cliente

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)

        if id:
            queryset = Cliente.objects.filter(id=id)
        else:
            queryset = Cliente.objects.all()

        return queryset

        