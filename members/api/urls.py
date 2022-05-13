# from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView
)

urlpatterns = [
	path('register/', UserCreateAPIView.as_view(), name='register'),                     # register api url
	path('login/', UserLoginAPIView.as_view(), name='login'),                     # register api url 

	# path('ajax/load-citys/', views.load_citys, name='ajax_load_citys'),
]  