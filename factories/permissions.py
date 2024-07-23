from home.permissions import GroupCondPermission
from factories.models import FactoryStaff

class FactoryPermission(GroupCondPermission):

    perm_codename = 'save_factory'

    allowed_actions = ['retrieve', 'list', 'create']
    obj_allowed_actions = allowed_actions

    def has_perm_cond(self, request, view):
        if view.action == 'create':
            self.user_allowed_statuses = []
        else:
            self.user_allowed_statuses = ['Active']
        return super().has_perm_cond(request, view)

    def has_object_perm_cond(self, request, view, obj):
        return FactoryStaff.objects.filter(factory=obj, user=request.user)

# class FactoryActivationPermission(GroupPermission):
#     pass
