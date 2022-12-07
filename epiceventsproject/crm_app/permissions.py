from rest_framework import permissions

"""CUSTOM PERMISSIONS"""


# groups permissions
class GroupsPerms(permissions.BasePermission):
    # django basics perms (get, head, options)
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    # django basics obj perms (get, head, options)
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


# permissions for sales_team
# todo: restreindre methode DEL (seuls les admins)
# - []  Créer des clients
# - []  Afficher et mettre à jour les clients (qui leur sont attribués)
# - []  Afficher et modifier les contrats (des clients qui leur sont attribués)
# - []  Créer des événements pour un contrat
class SalesTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        print("sales sales perm")
        # role sales_team
        if request.user.role == 3:
            return True
        return False


# permissions for support_team
# - [x]  Afficher et mettre à jour les événements (qui leur sont attribués)
# - [x]  Afficher les clients (pour les clients des événements qui leur sont attribués)
class SupportTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        print("sales support perm")
        # role support_team
        if request.user.role == 2:
            return True
        return False
