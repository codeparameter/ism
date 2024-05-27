from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import routes

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(routes)),
]