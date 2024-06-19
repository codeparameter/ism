
from .viewsets import *

routepatterns = [
    (('pics', PicViewSet), {'basename':'pics'}),
    (('vids', VidViewSet), {'basename': 'vids'}),
]