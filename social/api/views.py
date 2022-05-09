# LOGIC .. similair to post-list 

# from rest_framework.generics import ListAPIView      # https://www.django-rest-framework.org/api-guide/generic-views/#listapiview
# from posts.models import Post
# from posts.api.serializers import PostSerializer

# class PostListAPIView(ListAPIView):                  # this can do the same logic as post_list function in posts/views.py                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer


# NOTES !!!!!!!!!!!!! 

# working with the coding below ... if we run localhost:8000/api/posts  .. we will land the drf page which will display the posts using logic ...
# ... from PostListApiView, data displayed in serialzed data format
# if we go to localhost:8000/create we will land the create page to create a post with the fields from serialzers.py .. go back to api/posts/ to view
# if we go to /api/posts/?format=json the posts data will be displayed in json format 

# api/serializers.py:
# from rest_framework.serializers import ModelSerializer
# from posts.models import Post
# class PostListSerializer(ModelSerializer):
# 	class Meta:
# 		model = Post 
# 		fields = {
# 			'title',
# 			'slug',
# 			'content',
# 		}


# api/urls.py:
# url(r'^$', PostListAPIView.as_view(), name='list'),   
#...............................................................................




















# LOGIC .. similiar to post-detail 

# from rest_framework.generics import ListAPIView, RetrieveAPIView 
# from posts.models import Post
# from posts.api.serializers import PostListSerializer, PostDetailSerializer

# class PostListAPIView(ListAPIView):                               
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class PostDetailAPIView(RetrieveAPIView):                               # this can do the same logic as posts/views.py post_detail function 
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer



# NOTES !!!!!!!!!!!!!

# created a postdetailserialzer class and url 
# with the below coding ... we can go to localhost:8000/api/posts/3/   ... and view the post with the pk 3 ... post-detail concept 

# serializer.py
# from rest_framework.serializers import ModelSerializer
# from posts.models import Post
# class PostDetailSerializer(ModelSerializer):               # serializer for the post detial 
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'id',
# 			'title',
# 			'slug',
# 			'content',
# 			'publish'
# 		]


# urls.py 
# urlpatterns = [
# 	url(r'^$', PostListAPIView.as_view(), name='list'),                         
# 	url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
# ]
#...............................................................................





# from rest_framework.generics import ListAPIView, RetrieveAPIView 
# from posts.models import Post
# from posts.api.serializers import PostListSerializer, PostDetailSerializer

# class PostListAPIView(ListAPIView):                               
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer
# 	lookup_field = 'slug'                                # using drf lookup_feild on field slug .. so url will be based on slug field not the pk 




# NOTES !!!!!!!!!!!!!

# edited the detail url ... get post detail based on slug now  

# urls.py 
# urlpatterns = [
# 	url(r'^$', PostListAPIView.as_view(), name='list'),                         
# 	url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail')       # url based on the slug .. usually we do based on pk 
# ]
# ..................................................................




















# # LOGIC ... similar to post_update and delete  

# from rest_framework.generics import DestroyAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView    # added apiviews  
# from posts.models import Post
# from posts.api.serializers import PostListSerializer, PostDetailSerializer

# class PostDeleteAPIView(DestroyAPIView):                  # added for delete logic                             
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostListAPIView(ListAPIView):                               
# 	queryset = Post.objects.all()
# 	serializer_class = PostListSerializer

# class PostUpdateAPIView(UpdateAPIView):                    # added class for update logic                          
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 



# NOTES !!!!!!!!!!!1

# added update and delete urls:
# url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),   # url to update a post 
# url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'), # url to delete 

# now we can go to http://localhost:5000/api/posts/2/edit/ and successfully edit this post
# now we can go to http://localhost:5000/api/posts/2/delete/ and successfully delete this post
# CANNOT DO http://localhost:5000/api/posts/yeah-buddy/delete/  since the slug (yeah-buddy) is for get 
# ...........................................................





















# LOGIC ... create logic 

# from rest_framework.generics import ( 
# 	CreateAPIView,    # added createapiviews 
# 	DestroyAPIView, 
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	UpdateAPIView
# 	)     
# from posts.models import Post
# from posts.api.serializers import PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer

# class PostCreateAPIView(CreateAPIView):                  # added for create logic                             
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer	

# class PostDeleteAPIView(DestroyAPIView):                                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostListAPIView(ListAPIView):                               
# 	queryset = Post.objects.all()
# 	serializer_class = PostListSerializer

# class PostUpdateAPIView(UpdateAPIView):                                             
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	lookup_field = 'slug' 



# NOTES !!!!!!!!!!!!

# we can go to localhost:8000/api/posts/create   .. to create a post 
#...............................................................

















# LOGIC ... associate user with view methods ... autofill existing fields in forms like when we edit a post 

# from rest_framework.generics import ( 
# 	CreateAPIView,    # added createapiviews 
# 	DestroyAPIView, 
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	RetrieveUpdateAPIView,            # added ... this will help to autofill exisitng data in feilds 
# 	UpdateAPIView
# 	)     
# from posts.models import Post
# from posts.api.serializers import (PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer)


# class PostCreateAPIView(CreateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer

# 	def perform_create(self, serializer):               # added function 
# 		serializer.save(user=self.request.user)         # this will set the user field
# 														# we did this so when a post is created ..  the user who posted there id number is displayed
	
# class PostDeleteAPIView(DestroyAPIView):                                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug' 

# class PostListAPIView(ListAPIView):                               
# 	queryset = Post.objects.all()
# 	serializer_class = PostListSerializer

# class PostUpdateAPIView(RetrieveUpdateAPIView):         # edit to retrieve                                     
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	lookup_field = 'slug' 

# 	def perform_update(self, serializer):               # added function 
# 		serializer.save(user=self.request.user)			# this will set the user field 
														# we did this so when a post is edited ..  the user who edited there id number is displayed



# NOTES

# user id number displayed on posting a post and editing a post
# when user edits a post the fields are autofilled with that posts current data 
# .....................................................................................



















# LOGIC ..... custom user permissions 

from rest_framework.generics import ( 
	CreateAPIView,                    
	DestroyAPIView, 
	ListAPIView, 
	RetrieveAPIView, 
	RetrieveUpdateAPIView,             
	UpdateAPIView
	)     
from social.models import Post
from social.api.serializers import (PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer)

from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)    # added 
from social.api.permissions import IsOwnerOrReadOnly                                                           # added 


class PostCreateAPIView(CreateAPIView):                                              
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes = [IsAuthenticated]       # added IsAuthenticated .. user must be logged in to create post now if not error
															  
	def perform_create(self, serializer):               
		serializer.save(author=self.request.user)         
	
class PostDeleteAPIView(DestroyAPIView):                                           
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'id' 

class PostDetailAPIView(RetrieveAPIView):                                
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'id' 

class PostListAPIView(ListAPIView):                               
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):                                              
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # added IsAuthenticatedOrReadOnly .. user must be logged in to update post now if not error
																		 # added IsOwnerOrReadOnly we created in permissions.py
																		 # so now only the user who created the post can edit is or else error
	lookup_field = 'id' 

	def perform_update(self, serializer):                
		serializer.save(author=self.request.user)