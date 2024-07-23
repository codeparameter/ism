from home.permissions import GroupOrReadOnlyPermission
from mines.models import MineStaff

class BlockPermission(GroupOrReadOnlyPermission):

    perm_codename = 'save_block'

    def has_object_perm_cond(self, request, view, obj):
        return MineStaff.objects.filter(mine=obj.mine, user=request.user)