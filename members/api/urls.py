# from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserAPIView,
	UserProfileAPIView,
	UserUpdateAPIView
)

urlpatterns = [
	path('register/', UserCreateAPIView.as_view(), name='register-api'),                     # register api url
	path('login/', UserLoginAPIView.as_view(), name='login-api'),                     # register api url
	path('user/', UserAPIView.as_view(), name='user-api'), 
	path('user_profile/', UserProfileAPIView.as_view(), name='user-profile-api'), 
	path('user/edit/<username>/', UserUpdateAPIView.as_view(), name='user-update-api'), 

	# path('ajax/load-citys/', views.load_citys, name='ajax_load_citys'),
]  