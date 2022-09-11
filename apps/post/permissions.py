from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authentiacted and request.user == obj.author


class Permissions:
    def get_permission(self):
        if self.action == "create":
            permissions = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [
                IsAuthorPermission,
            ]
        else:
            permissions = []
        return [permission() for permission in permissions]
