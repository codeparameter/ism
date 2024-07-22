from rest_framework import mixins, viewsets

class PostViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):

    def post(self, request, *args, **kwargs):
        pass

    create = post