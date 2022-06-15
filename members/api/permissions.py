from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):                           
	message = 'You must be the owner of this object.'
	my_safe_method = ['GET', 'PUT']                                  # variable bound to only GET and PUT ... basically bound to updating a post only 

	def has_permission(self, request, view):                  # this function is to varify its a PUT method only 
		if request.method in self.my_safe_method:
			return True 
		return False

	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True 
		return obj.username == request.user      