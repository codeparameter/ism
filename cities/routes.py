
from .viewsets import *

routepatterns = [
    (('cities', CityViewSet), {'basename': 'cities'}),
]