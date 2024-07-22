
from .viewsets import *

routepatterns = [
    (('register', UserRegistrationViewSet), {'basename': 'register'}),
    (('verify-phone', UserPhoneVerificationViewSet), {'basename': 'verify-phone'}),
]