# LOGIC .... comments api 

from rest_framework.generics import ( 
	CreateAPIView,                    
	DestroyAPIView, 
	ListAPIView, 
	RetrieveAPIView, 
	RetrieveUpdateAPIView,             
	UpdateAPIView
	)     
from social.models import Post, Comment            # added comment model 
from social.api.serializers import (
CommentSerializer, 
CommentDetailSerializer, 
PostCreateUpdateSerializer, 
PostDetailSerializer, 
PostDetailCommentsSerializer,
PostListSerializer
) # added comments serializers

from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)    
from social.api.permissions import IsOwnerOrReadOnly      

from django.db.models import Q                                                                     

from rest_framework.filters import SearchFilter, OrderingFilter   

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination   



class CommentDetailAPIView(RetrieveAPIView):             # added same concept as postdetailapiview 
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer  
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'id' 

class CommentDeleteAPIView(DestroyAPIView):                                           
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]           
	lookup_field = 'id' 

class CommentListAPIView(ListAPIView):                    # added same concept of postlistapiview             
	# queryset = Post.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]                              
	search_fields = ['content', 'first_name', 'last_name', 'author']       
	pagination_class = PostPageNumberPagination                                     
																	  
	def get_queryset(self, *args, **kwargs):                                           
		# queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = Comment.objects.all()                                             
		query = self.request.GET.get("q")                                              
		if query:
			queryset_list = queryset_list.filter(                                      
				Q(comment__icontains=query)|     
				# Q(author__icontains=query)|                                                                                       
				# Q(image__icontains=query)|
				# Q(video__icontains=query)|
				Q(author__first_name__icontains=query) |                               
				Q(author__last_name__icontains=query)                                   
				).distinct()
		return queryset_list								            
                 

class PostCreateAPIView(CreateAPIView):                                              
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	# permission_classes = [IsAuthenticated]       
															  
	def perform_create(self, serializer):               
		serializer.save(author=self.request.user)         
	
class PostDeleteAPIView(DestroyAPIView):                                           
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]           
	lookup_field = 'id' 

class PostDetailAPIView(RetrieveAPIView):                                
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id' 

class PostDetailCommentsAPIView(RetrieveAPIView):                                
	queryset = Post.objects.all()
	serializer_class = PostDetailCommentsSerializer
	lookup_field = 'pk' 

class PostListAPIView(ListAPIView):                               
	# queryset = Post.objects.all()
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]                              
	search_fields = ['body', 'first_name', 'last_name', 'author']  
	permission_classes = [AllowAny]  
	# permission_classes = [IsAdminUser]   
	pagination_class = PostPageNumberPagination                                     
																	  
	def get_queryset(self, *args, **kwargs):                                           
		# queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = Post.objects.all()                                             
		query = self.request.GET.get("q")                                              
		if query:
			queryset_list = queryset_list.filter(                                      
				Q(body__icontains=query)|     
				# Q(author__icontains=query)|                                                                                       
				# Q(image__icontains=query)|
				# Q(video__icontains=query)|
				Q(author__first_name__icontains=query) |                               
				Q(author__last_name__icontains=query)                                   
				).distinct()
		return queryset_list															

class PostUpdateAPIView(RetrieveUpdateAPIView):                                              
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly]  
	lookup_field = 'id' 

	def perform_update(self, serializer):                
		serializer.save(author=self.request.user) 



# LOGIC !!!!!!!!! 
# now we can go to locaolhost:8000/api/social/comments to view a list of comments 
# now we can go to localhost:8000/api/social/comments/<int:id>/ to view that comments details which include the replies 












































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



















# LOGIC ..... query searching 

# from rest_framework.generics import ( 
# 	CreateAPIView,                    
# 	DestroyAPIView, 
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	RetrieveUpdateAPIView,             
# 	UpdateAPIView
# 	)     
# from social.models import Post
# from social.api.serializers import (PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer)

# from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)    
# from social.api.permissions import IsOwnerOrReadOnly      

# from django.db.models import Q                                          # added                           


# class PostCreateAPIView(CreateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticated]       
															  
# 	def perform_create(self, serializer):               
# 		serializer.save(author=self.request.user)         
	
# class PostDeleteAPIView(DestroyAPIView):                                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'id' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'id' 

# class PostListAPIView(ListAPIView):                               
# 	# queryset = Post.objects.all()
# 	serializer_class = PostListSerializer

# 	def get_queryset(self, *args, **kwargs):                                          # added function 
# 		# queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
# 		queryset_list = Post.objects.all()                                             # CV = to all post objects
# 		query = self.request.GET.get("q")                                              # CV = self.request getting q ... use q for searching for a query
# 		if query:
# 			queryset_list = queryset_list.filter(                                      
# 				Q(body__icontains=query)|                                               # can search query by body 
# 				# Q(image__icontains=query)|
# 				# Q(video__icontains=query)|
# 				Q(author__first_name__icontains=query) |                                # can search by query by authors(User) first name
# 				Q(author__last_name__icontains=query)                                   # can search by query by authors(User) last name
# 				).distinct()
# 		return queryset_list															# will return all objects related to the query we searched 

# class PostUpdateAPIView(RetrieveUpdateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  
# 	lookup_field = 'id' 

# 	def perform_update(self, serializer):                
# 		serializer.save(author=self.request.user)



# NOTES !!!!!!!!!!!!!!!!!!!!
# we can go to http://localhost:7000/api/social/?q=chetram     ... this will search for posts with the authors first name chetram, last name, or body of the post 
# .....................................................................................





# #  LOGIC .... another way to filter querys 

# from rest_framework.generics import ( 
# 	CreateAPIView,                    
# 	DestroyAPIView, 
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	RetrieveUpdateAPIView,             
# 	UpdateAPIView
# 	)     
# from social.models import Post
# from social.api.serializers import (PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer)

# from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)    
# from social.api.permissions import IsOwnerOrReadOnly      

# from django.db.models import Q                                                                     

# from rest_framework.filters import SearchFilter, OrderingFilter                      # added these types of filters for getting querys 

# class PostCreateAPIView(CreateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticated]       
															  
# 	def perform_create(self, serializer):               
# 		serializer.save(author=self.request.user)         
	
# class PostDeleteAPIView(DestroyAPIView):                                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'id' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'id' 

# class PostListAPIView(ListAPIView):                               
# 	# queryset = Post.objects.all()
# 	serializer_class = PostListSerializer
# 	filter_backends = [SearchFilter, OrderingFilter]                               # added .. CV = searchfilter , orderingfilter
# 	search_fields = ['body', 'first_name', 'last_name', 'author']                  # added .. fields we can search by 

# 	def get_queryset(self, *args, **kwargs):                                           
# 		# queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
# 		queryset_list = Post.objects.all()                                             
# 		query = self.request.GET.get("q")                                              
# 		if query:
# 			queryset_list = queryset_list.filter(                                      
# 				Q(body__icontains=query)|     
# 				# Q(author__icontains=query)|                                                                                       
# 				# Q(image__icontains=query)|
# 				# Q(video__icontains=query)|
# 				Q(author__first_name__icontains=query) |                               
# 				Q(author__last_name__icontains=query)                                   
# 				).distinct()
# 		return queryset_list															

# class PostUpdateAPIView(RetrieveUpdateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  
# 	lookup_field = 'id' 

# 	def perform_update(self, serializer):                
# 		serializer.save(author=self.request.user)



# NOTES !!!!!!!!!!!
# we can do same concept as previous coding with the search filter
# http://localhost:7000/api/social/?q=chetram&q=bassit  .. we can do a double search now .. and this is with the searchfilter
# with orderingfilter we can do http://localhost:7000/api/social/?q=chetram&ordering=body .. will show posts in order based on body 
# with orderingfilter we can do http://localhost:7000/api/social/?q=chetram&ordering=-body .. will show posts in reverse order based on body




















# #  LOGIC .... Pagination with Rest Framework .... create pagination.py file in api folder 

# from rest_framework.generics import ( 
# 	CreateAPIView,                    
# 	DestroyAPIView, 
# 	ListAPIView, 
# 	RetrieveAPIView, 
# 	RetrieveUpdateAPIView,             
# 	UpdateAPIView
# 	)     
# from social.models import Post
# from social.api.serializers import (PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer)

# from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)    
# from social.api.permissions import IsOwnerOrReadOnly      

# from django.db.models import Q                                                                     

# from rest_framework.filters import SearchFilter, OrderingFilter   

# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination                  # added
                 

# class PostCreateAPIView(CreateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticated]       
															  
# 	def perform_create(self, serializer):               
# 		serializer.save(author=self.request.user)         
	
# class PostDeleteAPIView(DestroyAPIView):                                           
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]           # also added this to delete so user must be owner of post to delete 
# 	lookup_field = 'id' 

# class PostDetailAPIView(RetrieveAPIView):                                
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'id' 

# class PostListAPIView(ListAPIView):                               
# 	# queryset = Post.objects.all()
# 	serializer_class = PostListSerializer
# 	filter_backends = [SearchFilter, OrderingFilter]                              
# 	search_fields = ['body', 'first_name', 'last_name', 'author']       
# 	pagination_class = PostPageNumberPagination                                     
																	  
# 	def get_queryset(self, *args, **kwargs):                                           
# 		# queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
# 		queryset_list = Post.objects.all()                                             
# 		query = self.request.GET.get("q")                                              
# 		if query:
# 			queryset_list = queryset_list.filter(                                      
# 				Q(body__icontains=query)|     
# 				# Q(author__icontains=query)|                                                                                       
# 				# Q(image__icontains=query)|
# 				# Q(video__icontains=query)|
# 				Q(author__first_name__icontains=query) |                               
# 				Q(author__last_name__icontains=query)                                   
# 				).distinct()
# 		return queryset_list															

# class PostUpdateAPIView(RetrieveUpdateAPIView):                                              
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  
# 	lookup_field = 'id' 

# 	def perform_update(self, serializer):                
# 		serializer.save(author=self.request.user) 



# NOTES !!!!!!!!!!!!!11
# pagination set up using pagination.py and importing those classes into our Post list api view 






















