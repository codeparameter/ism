from django.urls import path, include

urlpatterns = [
    path('blocks/', include('blocks.api_urls')),
]