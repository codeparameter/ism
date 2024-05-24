from rest_framework.routers import DefaultRouter

router = DefaultRouter()
routepatterns = []

def include(_from):
    exec(f"from {_from} import routepatterns as rp")
    exec(f"routepatterns += rp")

def register_routes():
    for args, kwargs in routepatterns:
        router.register(*args, **kwargs)
    return router.urls
       