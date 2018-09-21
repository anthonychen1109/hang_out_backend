from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        if a request contains HTTP verbs GET, OPTIONS, HEAD- then it is
        read-only request and permission is granted
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        """
        write permissions are only allowed to the creator of the event
        """
        return obj.event == request.user
