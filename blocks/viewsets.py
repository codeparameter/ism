from rest_framework import mixins, viewsets
from .serializers import *


class BlockPicViewSet(viewsets.ModelViewSet):
    queryset = BlockPic.objects.all()
    serializer_class = BlockPicSerializer


class BlockVidViewSet(viewsets.ModelViewSet):
    queryset = BlockVid.objects.all()
    serializer_class = BlockVidSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class QualityGenericViewSet(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer