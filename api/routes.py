from .router import include, register_routes

include('files.routes')
include('phones.routes')
include('cities.routes')
include('mines.routes')
include('blocks.routes')
include('users.routes')

urlpatterns = register_routes()