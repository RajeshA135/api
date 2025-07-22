from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners (admins) to edit/delete,
    others (non-admins) can only read (GET).
    """

    def has_permission(self, request, view):
        # Allow GET for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow full access only if user is admin (is_staff=True)
        return request.user and request.user.is_authenticated and request.user.is_staff
