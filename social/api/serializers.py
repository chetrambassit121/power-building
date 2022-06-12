# notes .. put classes in alphebetical order .. easier for other coders to find a class .. created order will be mark with a number 







# from rest_framework.serializers import ModelSerializer

# from social.models import Post

# class PostCreateUpdateSerializer(ModelSerializer):                   # serialzer for the post create (3) 
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			# 'id',
# 			'title',
# 			# 'slug',
# 			'content',
# 			'publish'
# 		]


# class PostDetailSerializer(ModelSerializer):               # serializer for the post detial (2)
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'id',
# 			'title',
# 			'slug',
# 			'content',
# 			'publish'
# 		]

# class PostListSerializer(ModelSerializer):                   # serialzer for the post list (1) 
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'user',
# 			'id',
# 			'title',
# 			'slug',
# 			'content',
# 			'publish'
# 		]

#NOTES !!!!!!!!!!!!!!!1
# these fields are based on his Post model not mines 




















# LOGIC .... adding Hyperlinked Identity Field for URL

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField               # added hyperlink 

# from social.models import Post

# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# class PostDetailSerializer(ModelSerializer):               
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags'
# 		]

# class PostListSerializer(ModelSerializer):        
# 	url = HyperlinkedIdentityField(                                     # added .. this url will lead to the post-detail page
# 		# view_name='social-api:detail',                                # name from powerbuilding.urls the api/social path 
# 																		# : along with DETAIL name from api.urls detail path 
# 		view_name='detail',                                             # had to remove social-api name was getting an error ... 
# 																		# just detail name from detail url works as well    
#  		lookup_field='id'                                               # id as lookupfield 
# 	)           

# 	delete_url = HyperlinkedIdentityField(                              # added .. this url will lead to the post delete page 
# 		# view_name='social-api:delete',                                # name from powerbuilding.urls the api/social path 
# 																		# : along with DELETE name from api.urls delete path 
# 		view_name='delete',                                             # had to remove social-api name was getting an error ... 
# 																		# just delete name from delete url works as well    
#  		lookup_field='id'                                               # id as lookupfield 
# 	)           
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                      # added url as field now 
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 # added delete_url 
# 		]



# # NOTES !!!!!!!!!!!!!!
# # url links to view DETAIL AND DELETE pages are now added to our post-list page 
# ........................................................................................





# # LOGIC .... cleaner way of creating detail and delete hyperlinks 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField                

# from social.models import Post

# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      # added ... CV = the logic for post-detail hyperlink 

# class PostDetailSerializer(ModelSerializer):       
# 	url = post_detail_url                                                              # added ... CV = postdetailurl variable 
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                    # added the url variable 
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags'
# 		]

# class PostListSerializer(ModelSerializer):        
# 	url = post_detail_url                                                           # added .. url varible 
# 	delete_url = HyperlinkedIdentityField(                             
# 		view_name='delete',                                             													
#  		lookup_field='id'                                               
# 	)           
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                       
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 
# 		]



# # NOTES !!!!!!!!!!!!!!
# # this is a cleaner way to display our post-detail hyperlink ..... in tutoiral he removed the delete hyperlink i will keep it.
# # ...............................................................................................





















# # LOGIC .... return author string instead of id ......get image hyperlink .. added get html code with markdown ... 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField                      

# from social.models import Post
# from members.models import User



# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      

# class PostDetailSerializer(ModelSerializer):       
# 	url = post_detail_url                                                              
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags'
# 		]

# class PostListSerializer(ModelSerializer):   
# 	author = SerializerMethodField()                          # CV = to the method  ...  will help us retrive author string name  
# 	# image = SerializerMethodField()                          # CV = to the method  ... for image .... not needed for our posts ...
# 	html = SerializerMethodField()                            # CV = method ... for getting the html code of the posts body 
# 	url = post_detail_url                                                           
# 	delete_url = HyperlinkedIdentityField(                             
# 		view_name='delete',                                             													
#  		lookup_field='id'                                               
# 	)           
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'url',                                                       
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'html',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 
# 		]

# 	def get_author(self, obj):                       # added this function to return author string instead of id number 
# 		return str(obj.author.username)              # so this will get the actual authors string name 

# 	# def get_image(self, obj):                      # we did not need this for our image hyperlink .. this is another way to return image field and link 
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                          # added function get get the html code of the body of that post 
# 		return obj.get_markdown()



# # NOTES !!!!!!!!!!!!!!
# # basically returned author name instead of id number , image coding not needed for our posts,  and implemeted getting the hmtl (markdown) code of the posts body 
# # ...............................................................................................




















# # LOGIC .... comments api with replies 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField                      

# from social.models import Post, Comment                                     # added Comment 
# from members.models import User


# class CommentSerializer(ModelSerializer):                    # added comment serilaizer same concept as postserializer 
# 	author = SerializerMethodField()       
# 	reply_count = SerializerMethodField()         
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'parent',
# 			'tags',	
# 			'reply_count'
# 		]

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# class CommentChildSerializer(ModelSerializer):                    # added 
# 	author = SerializerMethodField()                
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			# 'likes',
# 			# 'dislikes',
# 			'parent',
# 			# 'tags'	
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)


# class CommentDetailSerializer(ModelSerializer):                    # added  
# 	author = SerializerMethodField()    
# 	replies = SerializerMethodField()    
# 	reply_count = SerializerMethodField()           
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'tags', 
# 			'replies',
# 			'reply_count'
# 		]



# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# 	def get_replies(self, obj):                                   # this function basically serializes our replies data 
# 		if obj.is_parent:
# 			return CommentChildSerializer(obj.children(), many=True).data     # return the replies related to parent comment 
# 		return None

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0


# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      

# class PostDetailSerializer(ModelSerializer):       
# 	url = post_detail_url                                                              
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags'
# 		]

# class PostListSerializer(ModelSerializer):   
# 	author = SerializerMethodField()                           
# 	# image = SerializerMethodField()                          
# 	html = SerializerMethodField()                             
# 	url = post_detail_url                                                           
# 	delete_url = HyperlinkedIdentityField(                             
# 		view_name='delete',                                             													
#  		lookup_field='id'                                               
# 	)           
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'url',                                                       
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'html',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()



# # NOTES !!!!!!!!!!!!!!
# # created serlizer for comment list, and comment details
# # ...............................................................................................





















# # LOGIC ....  Comments in Post Detail API View .... FAILED TO DO THIS 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField                      

# from social.models import Post, Comment                                     
# from members.models import User



# class CommentSerializer(ModelSerializer):                     
# 	author = SerializerMethodField()       
# 	reply_count = SerializerMethodField()         
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'parent',
# 			'tags',	
# 			'reply_count'
# 		]

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# class CommentChildSerializer(ModelSerializer):                    
# 	author = SerializerMethodField()                
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			# 'likes',
# 			# 'dislikes',
# 			'parent',
# 			# 'tags'	
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)


# class CommentDetailSerializer(ModelSerializer):                      
# 	author = SerializerMethodField()    
# 	replies = SerializerMethodField()    
# 	reply_count = SerializerMethodField()           
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'tags', 
# 			'replies',
# 			'reply_count'
# 		]



# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# 	def get_replies(self, obj):                                   
# 		if obj.is_parent:
# 			return CommentChildSerializer(obj.children(), many=True).data      
# 		return None

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0


# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      
# class PostDetailSerializer(ModelSerializer):       
# 	url = post_detail_url
# 	author = SerializerMethodField()                           
# 	html = SerializerMethodField()   
# 	# comments = SerializerMethodField()                                                                               
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'html',
# 			# 'comments'
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()

# 	# def get_comments(self, obj):
# 	# 	# content_type = obj.get_content_type
# 	# 	# object_id = obj.id
# 	# 	# c_qs = Comment.objects.filter(obj)
# 	# 	# comments = CommentSerializer(c_qs, many=True).data 
# 	# 	# return comments 



# 	# 	obj = Post.objects.filter(pk=pk)
# 	# 	c_qs = Comment.objects.filter(obj=obj)
# 	# 	comments = CommentSerializer(c_qs, many=True).data 
# 	# 	return comments 

# class PostDetailCommentsSerializer(ModelSerializer):       
# 	url = post_detail_url
# 	author = SerializerMethodField()                           
# 	html = SerializerMethodField()   
# 	comments = SerializerMethodField()                                                                               
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'pk',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'html',
# 			'comments'
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()

# 	def get_comments(self, pk):
# 		post = Post.objects.get(pk=pk)
# 		c_qs = Comment.objects.filter(post=post)
# 		comments = CommentSerializer(c_qs, many=True).data 
# 		return comments 

# class PostListSerializer(ModelSerializer):   
# 	author = SerializerMethodField()                           
# 	# image = SerializerMethodField()                          
# 	html = SerializerMethodField()                             
# 	url = post_detail_url                                                           
# 	delete_url = HyperlinkedIdentityField(                             
# 		view_name='delete',                                             													
#  		lookup_field='id'                                               
# 	)           
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'url',                                                       
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'html',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()



# # NOTES !!!!!!!!!!!!!!
# # tried to return comments to post detail ... failed to do so ... the get_comment() function isnt returning the comments smh 
# # ...............................................................................................





















# # LOGIC ....  Comments Create Serialzer function .... skipped 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError                      

# from social.models import Post, Comment                                     
# from members.models import User

# from django.contrib.contenttypes.models import ContentType


# def create_comment_serializer(id, model_type='post', parent_id=None):
# 	class CommentCreateSerializer(ModelSerializer):
# 		class Meta: 
# 			model = Comment
# 			fields = [
# 				'id',
# 				'comment',
# 				# 'created_on',
# 				# 'author',
# 				# 'likes',
# 				# 'dislikes',
# 				'parent',
# 				'tags',	
# 				# 'reply_count'
# 			]

# 		def __init__(self, *args, **kwargs):
# 			self.model_type = model_type 
# 			self.id = id 
# 			self.parent_obj = None 
# 			if self.parent_id:
# 				parent_qs = Comment.objects.filter(id=parent_id)
# 				if parent_sq.exists() and parent_qs.count() ==1:
# 					self.parent_obj = parent_qs.first()
# 			return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

# 		def validate(self, data):
# 			model_type = self.model_type
# 			model_qs = ContentType.objects.filter(model=model_type)
# 			if not model_qs.exists() or model_qs.count() != 1:
# 				raise ValidationError("This is not a valid content type")
# 			SomeModel = model_qs.first().model_class()
# 			obj_qs = SomeModel.objects.filter(id=self.id)
# 			if not obj_qs.exists() or obj_qs.count() != 1:
# 				raise ValidationError("This is not a id for this content type")
# 			return data

# 	return CommentCreateSerializer

# class CommentSerializer(ModelSerializer):                     
# 	author = SerializerMethodField()       
# 	reply_count = SerializerMethodField()         
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'parent',
# 			'tags',	
# 			'reply_count'
# 		]

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# class CommentChildSerializer(ModelSerializer):                    
# 	author = SerializerMethodField()                
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			# 'likes',
# 			# 'dislikes',
# 			'parent',
# 			# 'tags'	
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)


# class CommentDetailSerializer(ModelSerializer):                      
# 	author = SerializerMethodField()    
# 	replies = SerializerMethodField()    
# 	reply_count = SerializerMethodField()           
# 	class Meta:
# 		model = Comment 
# 		fields = [
# 			'id',
# 			'comment',
# 			'created_on',
# 			'author',
# 			'likes',
# 			'dislikes',
# 			'tags', 
# 			'replies',
# 			'reply_count'
# 		]



# 	def get_author(self, obj):                       
# 		return str(obj.author.username)

# 	def get_replies(self, obj):                                   
# 		if obj.is_parent:
# 			return CommentChildSerializer(obj.children(), many=True).data      
# 		return None

# 	def get_reply_count(self, obj):
# 		if obj.is_parent:
# 			return obj.children().count()
# 		return 0


# class PostCreateUpdateSerializer(ModelSerializer):                   
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'body',
# 			'image',
# 			'video'	
# 		]


# post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      
# class PostDetailSerializer(ModelSerializer):       
# 	url = post_detail_url
# 	author = SerializerMethodField()                           
# 	html = SerializerMethodField()   
# 	# comments = SerializerMethodField()                                                                               
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'html',
# 			# 'comments'
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()
# 	## HIS CODING
# 	# def get_comments(self, obj):
# 	# 	# content_type = obj.get_content_type
# 	# 	# object_id = obj.id
# 	# 	# c_qs = Comment.objects.filter(obj)
# 	# 	# comments = CommentSerializer(c_qs, many=True).data 
# 	# 	# return comments 
# 	# MINES 
# 	# 	obj = Post.objects.filter(pk=pk)
# 	# 	c_qs = Comment.objects.filter(obj=obj)
# 	# 	comments = CommentSerializer(c_qs, many=True).data 
# 	# 	return comments 

# class PostDetailCommentsSerializer(ModelSerializer):       
# 	url = post_detail_url
# 	author = SerializerMethodField()                           
# 	html = SerializerMethodField()   
# 	comments = SerializerMethodField()                                                                               
# 	class Meta:
# 		model = Post 
# 		fields = [
# 			'url',                                                                     
# 			'pk',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'html',
# 			'comments'
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()

# 	def get_comments(self, pk):
# 		post = Post.objects.get(pk=pk)
# 		c_qs = Comment.objects.filter(post=post)
# 		comments = CommentSerializer(c_qs, many=True).data 
# 		return comments 

# class PostListSerializer(ModelSerializer):   
# 	author = SerializerMethodField()                           
# 	# image = SerializerMethodField()                          
# 	html = SerializerMethodField()                             
# 	url = post_detail_url                                                           
# 	delete_url = HyperlinkedIdentityField(                             
# 		view_name='delete',                                             													
#  		lookup_field='id'                                               
# 	)           
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'url',                                                       
# 			'id',
# 			'author',
# 			'shared_user',
# 			'body',
# 			'shared_body',
# 			'image',
# 			'video',
# 			'html',
# 			'created_on',
# 			'shared_on',
# 			'likes',
# 			'dislikes',
# 			'tags',
# 			'delete_url'                                                 
# 		]

# 	def get_author(self, obj):                       
# 		return str(obj.author.username)               

# 	# def get_image(self, obj):                     
# 	# 	try:
# 	# 		image = obj.image.url 
# 	# 	except:
# 	# 		image = None 
# 	# 	return image 

# 	def get_html(self, obj):                         
# 		return obj.get_markdown()



# # NOTES !!!!!!!!!!!!!!
# # 
# # ...............................................................................................





















# LOGIC .... adding user details 

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError                      

from social.models import Post, Comment                                     
from members.models import User                     # added 

from django.contrib.contenttypes.models import ContentType

from members.api.serializers import UserDetailSerializer    # added 


def create_comment_serializer(id, model_type='post', parent_id=None):
	class CommentCreateSerializer(ModelSerializer):
		class Meta: 
			model = Comment
			fields = [
				'id',
				'comment',
				# 'created_on',
				# 'author',
				# 'likes',
				# 'dislikes',
				'parent',
				'tags',	
				# 'reply_count'
			]

		def __init__(self, *args, **kwargs):
			self.model_type = model_type 
			self.id = id 
			self.parent_obj = None 
			if self.parent_id:
				parent_qs = Comment.objects.filter(id=parent_id)
				if parent_sq.exists() and parent_qs.count() ==1:
					self.parent_obj = parent_qs.first()
			return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

		def validate(self, data):
			model_type = self.model_type
			model_qs = ContentType.objects.filter(model=model_type)
			if not model_qs.exists() or model_qs.count() != 1:
				raise ValidationError("This is not a valid content type")
			SomeModel = model_qs.first().model_class()
			obj_qs = SomeModel.objects.filter(id=self.id)
			if not obj_qs.exists() or obj_qs.count() != 1:
				raise ValidationError("This is not a id for this content type")
			return data

	return CommentCreateSerializer

class CommentSerializer(ModelSerializer):                     
	# author = SerializerMethodField()      
	author = UserDetailSerializer() 
	reply_count = SerializerMethodField()         
	class Meta:
		model = Comment 
		fields = [
			'id',
			'comment',
			'created_on',
			'author',
			'likes',
			'dislikes',
			'parent',
			'tags',	
			'reply_count'
		]

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

	# def get_author(self, obj):                       # removed                
	# 	return str(obj.author.username)

class CommentChildSerializer(ModelSerializer):                    
	# author = SerializerMethodField()  
	author = UserDetailSerializer()                  # author is now the fields in this serializer .. so we are displaying those fields            
	class Meta:
		model = Comment 
		fields = [
			'id',
			'comment',
			'created_on',
			'author',
			# 'likes',
			# 'dislikes',
			'parent',
			# 'tags'	
		]

	# def get_author(self, obj):                     # removed        
	# 	return str(obj.author.username)


class CommentDetailSerializer(ModelSerializer):                      
	# author = SerializerMethodField()    
	author = UserDetailSerializer()          # author is now the fields in this serializer .. so we are displaying those fields
	replies = SerializerMethodField()    
	reply_count = SerializerMethodField()           
	class Meta:
		model = Comment 
		fields = [
			'id',
			'comment',
			'created_on',
			'author',
			'likes',
			'dislikes',
			'tags', 
			'replies',
			'reply_count'
		]



	# def get_author(self, obj):                       # removed          
	# 	return str(obj.author.username)

	def get_replies(self, obj):                                   
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data      
		return None

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0


class PostCreateUpdateSerializer(ModelSerializer):                   
	class Meta:
		model = Post 
		fields = [
			'body',
			'image',
			'video'	
		]


post_detail_url = HyperlinkedIdentityField(view_name='detail', lookup_field='id')      
class PostDetailSerializer(ModelSerializer):       
	url = post_detail_url
	# author = SerializerMethodField()   
	author = UserDetailSerializer(read_only=True)               # author is now the fields in this serializer .. so we are displaying those fields                                                  
	html = SerializerMethodField()   
	# comments = SerializerMethodField()                                                                               
	class Meta:
		model = Post 
		fields = [
			'url',                                                                     
			'id',
			'author',
			'shared_user',
			'body',
			'shared_body',
			'image',
			'video',
			'created_on',
			'shared_on',
			'likes',
			'dislikes',
			'tags',
			'html',
			# 'comments'
		]

	# def get_author(self, obj):                       
	# 	return str(obj.author.username)               

	# def get_image(self, obj):                     
	# 	try:
	# 		image = obj.image.url 
	# 	except:
	# 		image = None 
	# 	return image 

	def get_html(self, obj):                         
		return obj.get_markdown()
	## HIS CODING
	# def get_comments(self, obj):
	# 	# content_type = obj.get_content_type
	# 	# object_id = obj.id
	# 	# c_qs = Comment.objects.filter(obj)
	# 	# comments = CommentSerializer(c_qs, many=True).data 
	# 	# return comments 
	# MINES 
	# 	obj = Post.objects.filter(pk=pk)
	# 	c_qs = Comment.objects.filter(obj=obj)
	# 	comments = CommentSerializer(c_qs, many=True).data 
	# 	return comments 

class PostDetailCommentsSerializer(ModelSerializer):       
	url = post_detail_url
	# author = SerializerMethodField()  
	author = UserDetailSerializer(read_only=True)          # author is now the fields in this serializer .. so we are displaying those fields .. 
														   # read only  so user cannot edit the user deital serilaizer fields                                           

	html = SerializerMethodField()   
	comments = SerializerMethodField()                                                                               
	class Meta:
		model = Post 
		fields = [
			'url',                                                                     
			'pk',
			'author',
			'shared_user',
			'body',
			'shared_body',
			'image',
			'video',
			'created_on',
			'shared_on',
			'likes',
			'dislikes',
			'tags',
			'html',
			'comments'
		]

	# def get_author(self, obj):                    # removed          
	# 	return str(obj.author.username)               

	# def get_image(self, obj):                     
	# 	try:
	# 		image = obj.image.url 
	# 	except:
	# 		image = None 
	# 	return image 

	def get_html(self, obj):                         
		return obj.get_markdown()

	def get_comments(self, pk):
		post = Post.objects.get(pk=pk)
		c_qs = Comment.objects.filter(post=post)
		comments = CommentSerializer(c_qs, many=True).data 
		return comments 

class PostListSerializer(ModelSerializer):   
	# author = SerializerMethodField()     
	author = UserDetailSerializer()    # author is now the fields in this serializer .. so we are displaying those fields                    
	# image = SerializerMethodField()                          
	html = SerializerMethodField()                             
	url = post_detail_url                                                           
	delete_url = HyperlinkedIdentityField(                             
		view_name='delete',                                             													
 		lookup_field='id'                                               
	)           
	class Meta:
		model = Post
		fields = [
			'url',                                                       
			'id',
			'author',
			'slug',
			'shared_user',
			'body',
			'shared_body',
			'image',
			'video',
			'html',
			'created_on',
			'shared_on',
			'likes',
			'dislikes',
			'tags',
			'delete_url'                                                 
		]

	# def get_author(self, obj):                         # removed 
	# 	return str(obj.author.username)               

	# def get_image(self, obj):                     
	# 	try:
	# 		image = obj.image.url 
	# 	except:
	# 		image = None 
	# 	return image 

	def get_html(self, obj):                         
		return obj.get_markdown()



# NOTES !!!!!!!!!!!!!!
# now all our author fields will display its own dictinary of user information .. username, emai, first, last 
# ...............................................................................................






