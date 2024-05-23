from rest_framework.permissions import BasePermission
from .models import ROLES

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.roles == ROLES.ADMIN.value

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.roles == ROLES.USER.value
