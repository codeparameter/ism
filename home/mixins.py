from rest_framework import mixins, viewsets

class PostViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):

    def create(self, request, *args, **kwargs):
        pass

class GetViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):

    def list(self, request, *args, **kwargs):
        pass