from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from files.viewsets import add_pics_to_model_record
from .permissions import BlockPermission
from .serializers import *
from mines.models import Mine
from .filters import BlockFilter


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [BlockPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlockFilter

    def create(self, request, *args, **kwargs):
        mine_id = request.data.get('mine')

        if not mine_id: # validation
            return Response({'error': 'Bad request. mine_id is required'},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            mine = Mine.objects.get(id=mine_id)
        except Mine.DoesNotExist:
            return Response({'error': 'Bad request. mine_id was incorrect'},
                                status=status.HTTP_400_BAD_REQUEST)

        request.data._mutable= True

        request.data["ct"] = mine.city.id
        request.data["mtr"] = mine.material.id

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Exclude fields "ct" and "mtr" from the update

        request.data._mutable= True
        
        request.data.pop("ct", None)
        request.data.pop("mtr", None)
        
        mine_id = request.data.get('mine')

        if mine_id:
            try:
                mine = Mine.objects.get(id=mine_id)
                request.data["ct"] = mine.city.id
                request.data["mtr"] = mine.material.id
            except Mine.DoesNotExist:
                return Response({'error': 'Bad request. mine_id was incorrect'},
                                    status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_pics(self, request, pk=None):
        return add_pics_to_model_record(request, self.get_object())


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class QualityGenericViewSet(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer