from rest_framework import generics
from .serializers import *


class CityListCreateAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class SchemaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class QualityListAPIView(generics.ListAPIView):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer


class BlockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer