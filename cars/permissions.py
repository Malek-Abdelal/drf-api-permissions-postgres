from rest_framework import permissions

class IsOwnerOrReadOlny(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        
        return request.user == obj.owner or request.user.is_staff == 1
    




        # updated_column = list(request.data.keys())
        # if request.method in ['PATCH', 'PUT'] and request.user == obj.owner and len(updated_column) == 1 and 'color' in updated_column:
        #     return True
        # return request.user.is_staff == 1