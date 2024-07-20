from rest_framework import mixins, viewsets
from .serializers import *


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ActivityGenericViewSet(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class MineViewSet(viewsets.ModelViewSet):
    queryset = Mine.objects.all()
    serializer_class = MineSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable= True
        request.data["Activity"] = 1
        return super().create(request, *args, **kwargs)

class MineStaffViewSet(viewsets.ModelViewSet):
    queryset = MineStaff.objects.all()
    serializer_class = MineStaffSerializer
