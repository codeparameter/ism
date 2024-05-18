from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.BlockListCreateAPIView.as_view()),
    path('cities', api_views.CityListCreateAPIView.as_view()),
    path('materials', api_views.MaterialListCreateAPIView.as_view()),
    path('schemas', api_views.SchemaListCreateAPIView.as_view()),
    path('qualities', api_views.QualityListAPIView.as_view()),
]