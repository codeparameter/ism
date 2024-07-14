
from .viewsets import *

routepatterns = [
    (('color', ColorViewSet), {'basename': 'color'}),
    (('schemas', SchemaViewSet), {'basename': 'schemas'}),
    (('qualities', QualityGenericViewSet), {'basename': 'qualities'}),
    (('blocks', BlockViewSet), {'basename': 'blocks'}),
]