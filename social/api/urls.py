# from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
	CommentListAPIView,
	CommentDetailAPIView,
	PostCreateAPIView,
	PostDeleteAPIView, 
	PostListAPIView, 
	PostDetailAPIView, 
	PostUpdateAPIView
)

urlpatterns = [
	

 	# comments api urls
 	path('comments/', CommentListAPIView.as_view(), name='comments'),                             # url to display comment fields/data
 	path('comments/<int:id>/', CommentDetailAPIView.as_view(), name='comment-detail'),            # url to display comment fields/data including the replies 


 	# posts api urls 
    path('', PostListAPIView.as_view(), name='list'),                             # url to display posts fields/data     
    path('create/', PostCreateAPIView.as_view(), name='create'),                  # url to create post 
	path('post/<int:id>/', PostDetailAPIView.as_view(), name='detail'),           # url to display post detail fields/data
	path('post/edit/<int:id>/', PostUpdateAPIView.as_view(), name='update'),      # url to edit a post 
    path('post/delete/<int:id>/', PostDeleteAPIView.as_view(), name='delete'),    # url to delete a post 















	# path(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),   # url to update a post 
 #    path(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'), # url to delete 


# url(r'^$', PostListAPIView.as_view(), name='list'),                             # url to display posts similar to  url(r'^$', post_list, name='list')     
 #    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),                  # url to create post    
	# url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),        # url to display post detail .... url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	# url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),   # url to update a post 
 #    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'), # url to delete 

	# url(r'^$', post_list, name='list'),
    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]