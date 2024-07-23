from django.contrib.auth.models import Group, Permission, ContentType
from mines.models import Mine
from factories.models import Factory


ADMIN_PERMISSIONS = [
    Permission.objects.get_or_create(
        defaults={"name": "Can verify mines",},
        content_type=ContentType.objects.get_for_model(Mine),
        codename="verify_mines",
        )[0],
    Permission.objects.get_or_create(
        defaults={"name": "Can verify factories",},
        content_type=ContentType.objects.get_for_model(Factory),
        codename="verify_factories",
        )[0],
]


def authorize():

    admins, _ = Group.objects.get_or_create(name="Administrators")

    admins.permissions.set(ADMIN_PERMISSIONS)
