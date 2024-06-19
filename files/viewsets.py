import json

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


def add_pics_to_model_record(request, model_instance):
    pic_ids = request.data.get('pic_ids')

    if not pic_ids: # validation
        return Response({'error': 'Bad request. pic_ids is required'}, 
                            status=status.HTTP_400_BAD_REQUEST)

    try: # validation
        pic_ids = json.loads(pic_ids)
        assert(type(pic_ids) == list)
    except Exception as e:
        return Response({'error': 'Bad request. pic_ids must be a json array'}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    for pic_id in pic_ids:
        pic = Pic.objects.get(id=pic_id)
        if not pic:
            return Response({'error': f"Bad request. pic id {pic_id} doesn't exist"}, 
                                status=status.HTTP_400_BAD_REQUEST)
        model_instance.pics.append({'id': pic_id, 'url': f'{pic.pic}/'})
        pic.dependencies.append({'model': str(type(model_instance)), 'id': model_instance.id})
        pic.save()

    model_instance.save()
    return Response({'success': 'Update successful', 'data': model_instance.pics}, status=status.HTTP_200_OK)


class VidViewSet(viewsets.ModelViewSet):
    queryset = Vid.objects.all()
    serializer_class = VidSerializer