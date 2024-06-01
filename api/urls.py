from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import routes
from .views import ValidateToken

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('validate-token/', ValidateToken.as_view()),
    path('', include(routes)),
]