from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser

class GroupPermission(BasePermission):

    perm_codename = ''
    user_allowed_statuses = ['Active']

    def has_activity_perm(self, user):
        return user.activity.status in self.user_allowed_statuses

    def has_group_perm(self, user):
        return any(user.groups.filter(permissions__codename=self.perm_codename))

    def has_permission(self, request, view):
        user = request.user

        if isinstance(user, AnonymousUser):
            return False
        if self.user_allowed_statuses and \
            not self.has_activity_perm(user):
            return False
        if self.perm_codename:
            return self.has_group_perm(user)
        return True

class GroupCondPermission(GroupPermission):

    allowed_actions = []
    obj_allowed_actions = allowed_actions

    def has_perm_cond(self, request, view):
        return True

    def has_permission(self, request, view):
        if view.action in self.allowed_actions:
            return True
        return self.has_perm_cond(request, view) and \
                super().has_permission(request, view)

    def has_object_perm_cond(self, request, view, obj):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in self.obj_allowed_actions:
            return True
        return self.has_object_perm_cond(request, view, obj)

class GroupOrReadOnlyPermission(GroupCondPermission):
    
    allowed_actions = ['retrieve', 'list']
    obj_allowed_actions = allowed_actions

class GroupOrRetrievePermission(GroupCondPermission):
    
    allowed_actions = ['retrieve']
    obj_allowed_actions = allowed_actions