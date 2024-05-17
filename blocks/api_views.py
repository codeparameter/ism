from django.http import JsonResponse

def index(request, *args, **kwargs):
    return JsonResponse({"msg": "Hi"})