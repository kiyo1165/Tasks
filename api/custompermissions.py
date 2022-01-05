from rest_framework import permissions

#TaskViewSets用のCustomPermission
class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #get methodのみ許可
        if request.method in permissions.SAFE_METHODS:
            return True
        # get以外のmethodの場合はtask.ownerとリクエストユーザーが一致している場合のみTrue
        return obj.owner.id == request.user.id