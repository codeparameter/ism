from rest_framework.permissions import BasePermission


def has_group_perm(user, perm_codename):
    if user.activity.status is not 'Active':
        return False
    return any(user.groups.filter(permissions__codename=perm_codename))

class GroupPermission(BasePermission):

    perm_codename = ''

    def has_permission(self, request, view):
        return has_group_perm(request.user, self.perm_codename)

    def has_object_permission(self, request, view, obj):
        return has_group_perm(request.user, self.perm_codename)

class GroupCondPermission(GroupPermission):

    allowed_actions = []
    obj_allowed_actions = []

    def has_perm_cond(self, request, view):
        return True

    def test(self, request, view):
        if view.action in self.allowed_actions:
            return True
        return super().has_permission(request, view) and \
             self.has_perm_cond(request, view)

    def has_permission(self, request, view):
        if view.action in self.allowed_actions:
            return True
        return super().has_permission(request, view) and \
             self.has_perm_cond(request, view)

    def has_object_perm_cond(self, request, view, obj):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in self.obj_allowed_actions:
            return True
        return super().has_object_permission(request, view, obj) and \
             self.has_object_perm_cond(request, view, obj)

class GroupOrReadOnlyPermission(GroupCondPermission):
    
    allowed_actions = ['retrieve', 'list']
    obj_allowed_actions = ['retrieve', 'list']

class GroupOrRetrievePermission(GroupCondPermission):
    
    allowed_actions = ['retrieve']
    obj_allowed_actions = ['retrieve']