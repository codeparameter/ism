from rest_framework import viewsets
from .serializers import *


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MineViewSet(viewsets.ModelViewSet):
    queryset = Mine.objects.all()
    serializer_class = MineSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable= True
        request.data["Activity"] = 1
        return super().create(request, *args, **kwargs)
