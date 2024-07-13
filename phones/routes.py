
from .viewsets import *

routepatterns = [
    (('phones', PhoneViewSet), {'basename': 'phones'}),
]