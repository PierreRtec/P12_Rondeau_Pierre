from rest_framework import permissions

"""CUSTOM PERMISSIONS"""


class RolesPermissions(permissions.BasePermission):
    """
    Roles Permissions.
    If user is sales_team and if he had obj, he can retrieve or edit it.
    """
    # si je suis role support_team je peux uniquement GET PUT mes events (pas de POST, pas de DEL)

    # si je suis role sales_team je peux uniquement POST clients et GET PUT mes clients +
    # GET PUT clients contracts
    # + POST events contracts
    # si je ne suis pas management_team, je ne peux pas DELETE

    def has_permission(self, request, view):
        # permissions management_team all
        if request.user.role == 1:
            return True
        # check role support_team perms
        elif request.user.role == 2:
            if view.action in ("retrieve", "update") and view.action != "delete":
                return True
            return False
        # check role sales_team perms
        elif request.user.role == 3:
            if view.action in ("retrieve", "update", "create") and view.action != "delete":
                return True
            return False
