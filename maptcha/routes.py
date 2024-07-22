
from .viewsets import *

routepatterns = [
    (('get-captcha', GetCaptchaViewSet), {'basename': 'get-captcha'}),
]