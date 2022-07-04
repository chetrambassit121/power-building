# LOGIC .... USER API SETUP 

from rest_framework.generics import ( 
	CreateAPIView,                    
	DestroyAPIView, 
	ListAPIView, 
	RetrieveAPIView, 
	RetrieveUpdateAPIView,             
	UpdateAPIView
	)     

from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)        

from django.db.models import Q                                                                     

from rest_framework.filters import SearchFilter, OrderingFilter   

# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination 

from django.contrib.auth import get_user_model

from members.models import User, UserProfile

from .permissions import IsOwnerOrReadOnly

from .serializers import UserCreateSerializer, ModelSerializer, UserLoginSerializer, UserProfileSerializer, UserDetailSerializer, UserCreateUpdateSerializer, UserProfileUpdateSerializer

from rest_framework.response import Response                                 # added for login                    
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST          # added for login 
from rest_framework.views import APIView                                      # added for login 


class UserCreateAPIView(CreateAPIView):                                        # user create view accessing usercreateserilaizer class 
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
	# permission_classes = [AllowAny]
	# permission_classes = [IsAdminUser]



class UserLoginAPIView(APIView):                                                  # user login view 
	permission_classes = [AllowAny]
	# permission_classes = [IsAdminUser]
	
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):                                  # when user posts data to login 
		data = request.data 
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data 
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserAPIView(ListAPIView):                                
	queryset = User.objects.all()
	serializer_class = UserDetailSerializer
	permission_classes = [AllowAny]
	# lookup_field = 'pk' 


class UserUpdateAPIView(RetrieveUpdateAPIView):                                              
	queryset = User.objects.all()
	serializer_class = UserCreateUpdateSerializer
	# permission_classes = [IsOwnerOrReadOnly] 
	permission_classes = [IsAuthenticatedOrReadOnly]   
	lookup_field = 'id' 

	def perform_update(self, serializer):                
		serializer.save(username=self.request.user) 


class UserProfileAPIView(ListAPIView):                                
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = [AllowAny]
	# lookup_field = 'pk' 

class UserProfileUpdateAPIView(RetrieveUpdateAPIView):                                              
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly] 
	# permission_classes = [IsAuthenticated]   
	lookup_field = 'username' 

	def perform_update(self, serializer):                
		serializer.save(username=self.request.user) 






