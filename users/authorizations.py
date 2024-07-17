from django.contrib.auth.models import Group, Permission, ContentType
from mines.models import Mine, MineStaff
from factories.models import Factory, FactoryStaff


# ADMIN_PERMISSIONS = [
#     Permission.objects.get_or_create(
#         defaults={"name": "Can verify mines",},
#         content_type=ContentType(Mine),
#         codename="verify_mines",
#         )[0],
#     Permission.objects.get_or_create(
#         defaults={"name": "Can verify mine staffs",},
#         content_type=ContentType(MineStaff),
#         codename="verify_mine_staffs",
#         )[0],
#     Permission.objects.get_or_create(
#         defaults={"name": "Can verify factories",},
#         content_type=ContentType(Factory),
#         codename="verify_factories",
#         )[0],
#     Permission.objects.get_or_create(
#         defaults={"name": "Can verify factory staffs",},
#         content_type=ContentType(FactoryStaff),
#         codename="verify_factory_staffs",
#         )[0],
# ]


def authorize():

    admins, _ = Group.objects.get_or_create(name="Administrators")

    # admins.permissions.set(ADMIN_PERMISSIONS)

    for app in (
        'mines',
        'factories',
    ):            
        exec(f"from {app}.authorizations import authorize as au")
        exec("au()")
