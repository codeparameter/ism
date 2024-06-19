import json

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from files.models import Pic, Vid
from .serializers import *


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    @action(detail=True, methods=['post'])
    def add_pics(self, request, pk=None):
        block = self.get_object()

        pic_ids = request.data.get('pic_ids')

        if not pic_ids:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        pic_ids = json.loads(pic_ids)
        
        for pic_id in pic_ids:
            pic = Pic.objects.get(id=pic_id)
            if not pic:
                return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
            block.pics.append({'id': pic_id, 'url': f'{pic.pic}'})
            pic.dependencies.append({'model': 'Block', 'id': block.id})
            pic.save()

        block.save()

        return Response({'success': 'Update successful', 'data': block.pics}, status=status.HTTP_200_OK)


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