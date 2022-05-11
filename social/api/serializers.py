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





















# LOGIC .... Comments api 

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField                      

from social.models import Post, Comment                                     # added Comment 
from members.models import User


 # comment = models.TextField()
 #    created_on = models.DateTimeField(default=timezone.now)
 #    author = models.ForeignKey(User, on_delete=models.CASCADE)
 #    post = models.ForeignKey('Post', on_delete=models.CASCADE)
 #    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
 #    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
 #    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
 #    tags = models.ManyToManyField('Tag', blank=True)




class CommentSerializer(ModelSerializer):                    # added comment serilaizer same concept as postserializer 
	author = SerializerMethodField()                
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
			'tags'	
		]

	def get_author(self, obj):                       
		return str(obj.author.username)


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
			'tags'
		]

class PostListSerializer(ModelSerializer):   
	author = SerializerMethodField()                          # CV = to the method  ...  will help us retrive author string name  
	# image = SerializerMethodField()                          # CV = to the method  ... for image .... not needed for our posts ...
	html = SerializerMethodField()                            # CV = method ... for getting the html code of the posts body 
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

	def get_author(self, obj):                       # added this function to return author string instead of id number 
		return str(obj.author.username)              # so this will get the actual authors string name 

	# def get_image(self, obj):                      # we did not need this for our image hyperlink .. this is another way to return image field and link 
	# 	try:
	# 		image = obj.image.url 
	# 	except:
	# 		image = None 
	# 	return image 

	def get_html(self, obj):                          # added function get get the html code of the body of that post 
		return obj.get_markdown()



# NOTES !!!!!!!!!!!!!!
# basically returned author name instead of id number , image coding not needed for our posts,  and implemeted getting the hmtl (markdown) code of the posts body 
# ...............................................................................................

