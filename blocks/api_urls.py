from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.BlockListCreateAPIView.as_view()),
    path('<int:pk>', api_views.BlockDetailAPIView.as_view()),
    path('<int:pk>/update/', api_views.BlockUpdateAPIView.as_view()),
    path('<int:pk>/delete', api_views.BlockDestroyAPIView.as_view()),
    path('pics/', api_views.BlockPicListCreateAPIView.as_view()),
    path('pics/<int:pk>', api_views.BlockPicDetailAPIView.as_view()),
    path('pics/<int:pk>/update/', api_views.BlockPicUpdateAPIView.as_view()),
    path('pics/<int:pk>/delete', api_views.BlockPicDestroyAPIView.as_view()),
    path('cities/', api_views.CityListCreateAPIView.as_view()),
    path('cities/<int:pk>/update/', api_views.CityUpdateAPIView.as_view()),
    path('cities/<int:pk>/delete/', api_views.CityDestroyAPIView.as_view()),
    path('materials/', api_views.MaterialListCreateAPIView.as_view()),
    path('materials/<int:pk>/update/', api_views.MaterialUpdateAPIView.as_view()),
    path('materials/<int:pk>/delete/', api_views.MaterialDestroyAPIView.as_view()),
    path('schemas/', api_views.SchemaListCreateAPIView.as_view()),
    path('schemas/<int:pk>/update/', api_views.SchemaUpdateAPIView.as_view()),
    path('schemas/<int:pk>/delete/', api_views.SchemaDestroyAPIView.as_view()),
    path('qualities/', api_views.QualityListAPIView.as_view()),
]