from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):                          # creating our own permission class 
	message = 'You must be the owner of this object.'
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user                           # user who created that object (post) must be the request.user 
																  # if not owner of object the message will be displayed 
# ..............................................................................


















# below coding didnt allow user to edit there own post kept getting error message 
# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsOwnerOrReadOnly(BasePermission):                           
# 	message = 'You must be the owner of this object.'
# 	my_safe_method = ['PUT']                                  # variable bound to only GET and PUT ... basically bound to updating a post only 

# 	def has_permission(self, request, view):                  # this function is to varify its a PUT method only 
# 		if request.method in self.my_safe_method:
# 			return True 
# 		else:
# 			return False

# 	def has_object_permission(self, request, view, obj):
# 		if request.method in SAFE_METHODS:
# 			return True 
# 		return obj.user == request.user                           