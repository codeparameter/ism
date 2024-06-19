from .router import include, register_routes

include('files.routes')
include('blocks.routes')

urlpatterns = register_routes()