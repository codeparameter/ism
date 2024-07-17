from django.contrib.auth.models import Group, Permission, ContentType


# FACTORY_STAFF_PERMISSIONS = [
# ]

# FACTORY_ACCOUNTER_PERMISSIONS = [
#     *FACTORY_STAFF_PERMISSIONS,
# ]

# FACTORY_MANAGER_PERMISSIONS = [
#     *FACTORY_STAFF_PERMISSIONS,
# ]

# FACTORY_OWNER_PERMISSIONS = [
#     *FACTORY_STAFF_PERMISSIONS,
#     # we can add all of the factory permissions for factory owners like this:
#     # *FACTORY_MANAGER_PERMISSIONS,
#     # *...
# ]

def authorize():

    factory_staffs, _ = Group.objects.get_or_create(name="FactoryStaffs")
    factory_accounters, _ = Group.objects.get_or_create(name="FactoryAccounters")
    factory_managers, _ = Group.objects.get_or_create(name="FactoryManagers")
    factory_owners, _ = Group.objects.get_or_create(name="FactoryOwners")

    # factory_staffs.permissions.set(FACTORY_STAFF_PERMISSIONS)
    # factory_accounters.permissions.set(FACTORY_ACCOUNTER_PERMISSIONS)
    # factory_managers.permissions.set(FACTORY_MANAGER_PERMISSIONS)
    # factory_owners.permissions.set(FACTORY_OWNER_PERMISSIONS)
