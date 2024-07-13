from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from files.viewsets import add_pics_to_model_record
from .serializers import *


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    @action(detail=True, methods=['post'])
    def add_pics(self, request, pk=None):
        return add_pics_to_model_record(request, self.get_object())


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class QualityGenericViewSet(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer