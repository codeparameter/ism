from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *


class PicViewSet(viewsets.ModelViewSet):
    queryset = Pic.objects.all()
    serializer_class = PicSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True  # Make the request data mutable
        pics = request.FILES.getlist('pic')
        result = []

        for pic in pics:
            request.data['pic'] = pic
            response = super().create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                result.append(response.data)
            else:
                return response  # If any pic fails, return the error

        return Response({'success': 'Creation successful', 'data': result}, status=status.HTTP_200_OK)      


class VidViewSet(viewsets.ModelViewSet):
    queryset = Vid.objects.all()
    serializer_class = VidSerializer