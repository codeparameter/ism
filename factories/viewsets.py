from rest_framework import mixins, viewsets
from .serializers import *

class ActivityGenericViewSet(
            mixins.ListModelMixin,
            viewsets.GenericViewSet
            ):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryStaffViewSet(viewsets.ModelViewSet):
    queryset = FactoryStaff.objects.all()
    serializer_class = FactoryStaffSerializer