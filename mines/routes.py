
from .viewsets import *

routepatterns = [
    (('materials', MaterialViewSet), {'basename': 'materials'}),
    (('mines', MineViewSet), {'basename': 'mines'}),
]