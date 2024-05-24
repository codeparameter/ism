
from .viewsets import *

routepatterns = [
    (('block-pics', BlockPicViewSet), {'basename':'block-pics'}),
    (('block-vids', BlockVidViewSet), {'basename': 'block-vids'}),
    (('blocks', BlockViewSet), {'basename': 'blocks'}),
    (('cities', CityViewSet), {'basename': 'cities'}),
    (('materials', MaterialViewSet), {'basename': 'materials'}),
    (('schemas', SchemaViewSet), {'basename': 'schemas'}),
    (('qualities', QualityGenericViewSet), {'basename': 'qualities'}),
]