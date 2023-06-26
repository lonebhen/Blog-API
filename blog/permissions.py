from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import View


class IsAuthorOnly(BasePermission):
    # message = "You are not allowed to carry out this task"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and view.get_queryset().filter(author=request.user).exists()

        return True

    def has_object_permission(self, request: Request, view, obj):
        return obj.author == request.user
