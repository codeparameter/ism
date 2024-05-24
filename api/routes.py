from .router import include, register_routes

include('blocks.routes')

urlpatterns = register_routes()