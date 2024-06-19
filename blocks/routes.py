
from .viewsets import *

routepatterns = [
    (('blocks', BlockViewSet), {'basename': 'blocks'}),
    (('cities', CityViewSet), {'basename': 'cities'}),
    (('materials', MaterialViewSet), {'basename': 'materials'}),
    (('schemas', SchemaViewSet), {'basename': 'schemas'}),
    (('qualities', QualityGenericViewSet), {'basename': 'qualities'}),
]