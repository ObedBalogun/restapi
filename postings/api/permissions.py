from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    #Object level permission to only allow owners of an object to edit it
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #instance must have an attribute named 'owner'
        return obj.owner == request.user #ref models --->