from rest_framework import generics
from .serializers import *


class CityListCreateAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityUpdateAPIView(generics.UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDestroyAPIView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialUpdateAPIView(generics.UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class SchemaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class SchemaUpdateAPIView(generics.UpdateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class SchemaDestroyAPIView(generics.DestroyAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class QualityListAPIView(generics.ListAPIView):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer


class BlockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockDetailAPIView(generics.RetrieveAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockUpdateAPIView(generics.UpdateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockDestroyAPIView(generics.DestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer