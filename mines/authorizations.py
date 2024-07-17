from django.contrib.auth.models import Group, Permission, ContentType
from blocks.models import Block


MINE_STAFF_PERMISSIONS = [
]

MINE_ACCOUNTER_PERMISSIONS = [
    *MINE_STAFF_PERMISSIONS,
]

MINE_SUPERVISOR_PERMISSIONS = [
    *MINE_STAFF_PERMISSIONS,
    Permission.objects.get_or_create(
        defaults={"name": "Can save block",},
        content_type=ContentType(Block),
        codename="save_block"
        )[0],
]

MINE_MANAGER_PERMISSIONS = [
    *MINE_STAFF_PERMISSIONS,
]

MINE_OWNER_PERMISSIONS = [
    *MINE_STAFF_PERMISSIONS,
    # we can add all of the mine permissions for mine owners like this:
    # *MINE_MANAGER_PERMISSIONS,
    # *...
]

def authorize():
    mine_staffs, _ =Group.objects.get_or_create(name="MineStaffs")
    mine_accounters, _ =Group.objects.get_or_create(name="MineAccounters")
    mine_supervisors, _ =Group.objects.get_or_create(name="MineSupervisors")
    mine_managers, _ =Group.objects.get_or_create(name="MineManagers")
    mine_owners, _ =Group.objects.get_or_create(name="MineOwners")

    # mine_staffs.permissions.set(MINE_STAFF_PERMISSIONS)
    # mine_accounters.permissions.set(MINE_ACCOUNTER_PERMISSIONS)
    mine_supervisors.permissions.set(MINE_SUPERVISOR_PERMISSIONS)
    # mine_managers.permissions.set(MINE_MANAGER_PERMISSIONS)
    # mine_owners.permissions.set(MINE_OWNER_PERMISSIONS)
