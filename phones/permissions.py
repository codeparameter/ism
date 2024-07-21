from rest_framework import permissions

class IsPhoneOwnerPermission(permissions.DjangoModelPermissions):
    pass
    # perms_map = {
    #     'GET': [],
    #     'OPTIONS': [],
    #     'HEAD': [],
    #     'POST': ['%(app_label)s.add_%(model_name)s'],
    #     'PUT': ['%(app_label)s.change_%(model_name)s'],
    #     'PATCH': ['%(app_label)s.change_%(model_name)s'],
    #     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    # }

    # def has_permission(self, request, view):
    #     return super().has_permission(request, view)

    # def has_object_permission(self, request, view, obj):
    #     # obj.owner == request.user
    #     return super().has_object_permission(request, view, obj)