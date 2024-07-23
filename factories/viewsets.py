from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import FactoryPermission
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
    permission_classes = [IsAuthenticatedOrReadOnly, FactoryPermission]


# class FactoryActivationViewSet(viewsets.ModelViewSet):
#     queryset = Factory.objects.all()
#     serializer_class = FactorySerializer
#     permission_classes = []


class FactoryStaffViewSet(viewsets.ModelViewSet):
    queryset = FactoryStaff.objects.all()
    serializer_class = FactoryStaffSerializer