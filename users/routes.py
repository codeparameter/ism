
from .viewsets import *

routepatterns = [
    (('register', UserRegistrationViewSet), {'basename': 'register'}),
]