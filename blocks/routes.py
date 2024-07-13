
from .viewsets import *

routepatterns = [
    (('schemas', SchemaViewSet), {'basename': 'schemas'}),
    (('qualities', QualityGenericViewSet), {'basename': 'qualities'}),
    (('blocks', BlockViewSet), {'basename': 'blocks'}),
]