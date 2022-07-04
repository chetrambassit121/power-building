# LOGIC .... user detail serializer 

from asyncore import write
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField # charfield                

from social.models import Post, Comment
                                   

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from members.models import User, UserProfile, State, City 

from django.db.models import Q              

class StateSerializer(ModelSerializer):
	class Meta:
		model = State 
		fields = {
			'name'
		}

class CitySerializer(ModelSerializer):
	class Meta:
		model = City
		fields = {
			'state',
			'name'
		}

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		state = StateSerializer()
		city = CitySerializer()
		fields = [
			'username',
			'email',
			'first_name',
			'last_name', 
			'state',
			'city'
		]

class UserCreateUpdateSerializer(ModelSerializer):                   
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name', 
			'state',
			'city'	
		]

# User = get_user_model()
class UserProfileSerializer(ModelSerializer):
	user = UserDetailSerializer() 
	class Meta:
		model = UserProfile
		fields = [
			'user',
			'first_name',
			'last_name', 
			'birth_date',
			'location',
			'bio',
			'followers',
			'followings',
			'website_url'
		]

class UserProfileUpdateSerializer(ModelSerializer):
	user = UserDetailSerializer() 
	class Meta:
		model = UserProfile
		fields = [
			'user',
			'first_name',
			'last_name', 
			'birth_date',
			'location',
			'bio',
			'followers',
			'followings',
			'website_url'
		]




class UserCreateSerializer(ModelSerializer):
	email = EmailField(label='Email Address')
	first_name = CharField(label="First Name")
	last_name = CharField(label="Last Name")
	state = State.objects.all()
	city = City.objects.filter(state=state)
	password = CharField(write_only=True)
	password2 = CharField(label="Re-enter Password", write_only=True)
	# email2 = EmailField(label='Confirm Email')
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
			'state',
			'city',
			'password',
			'password2',
		]

		# extra_kwargs = {
		# 	"password":{"write_only": True}, 
		# }
		


	def validate(self, data):
		# email = data['email']
		# user_qs = User.objects.filter(email=email)
		# if user_qs.exists():
		# 	raise ValidationError('User already exists')
		return data


	def validate_email(self, value):                               
		data = self.get_initial()
		email = data.get("email")
		# email2 = value
		# if email != email2:
		# 	raise ValidationError("Emails must match")
		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError('User already exists')
		return value 


	def validate_password2(self, value):                              
		data = self.get_initial()
		password = data.get("password")
		password2 = value
		if password != password2:
			raise ValidationError("Passwords must match")
		return value 


	def create(self, validated_data):                                
		# print(validated_data)
		username = validated_data['username']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		state = validated_data['state']
		city = validated_data['city']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
			username = username,
			email=email, 
			first_name=first_name,
			last_name=last_name,
			state=state,
			city=city
		)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data


class UserLoginSerializer(ModelSerializer):
	# password2 = PasswordField()
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True)
	email = EmailField(label='Email Adress', required=False, allow_blank=True)
	
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'token'
			# 'password2',
		]

		extra_kwargs = {"password":                                  
							{"write_only": True}
				}

	def validate(self, data):
		user_obj = None
		email = data.get('email', None)
		username = data.get('username', None)
		password=data["password"]
		if not username and not email:
			raise ValidationError("Username or email required to login")

		user = User.objects.filter(
			Q(email=email) |
			Q(username=username)
		).distinct()
		user = user.exclude(email__isnull=True).exclude(email__iexact="")
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError("This username/email is not valid")

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError('Inncorrect credentials')

		data["token"] = "SOME RANDOM TOKEN"

		return data


		# user_qs = User.objects.filter(email=email)
		# if user_qs.exists():
		# 	raise ValidationError('User already exists')

		



# NOTES !!!!!!!!!!!!!!!!!!
# we can go to localhost:8000/api/users/login/  ... user can login with email/username and password 





















# # LOGIC .... user detail serializer 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField # charfield                

# from social.models import Post, Comment
# from members.models import User                                     

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import get_user_model
# from members.models import User

# from django.db.models import Q              


# # User = get_user_model()

# class UserDetailSerializer(ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'first_name',
# 			'last_name', 
# 			'state',
# 			'city'
# 		]


# class UserCreateSerializer(ModelSerializer):
# 	# password2 = PasswordField()
# 	email = EmailField(label='Email Adress')
# 	email2 = EmailField(label='Confirm Email')
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'email2',
# 			'password'
# 			# 'password2',
# 		]

# 		extra_kwargs = {"password":                                  
# 							{"write_only": True}
# 				}

# 	def validate(self, data):
# 		# email = data['email']
# 		# user_qs = User.objects.filter(email=email)
# 		# if user_qs.exists():
# 		# 	raise ValidationError('User already exists')

# 		return data


# 	def validate_email(self, value):                               
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		user_qs = User.objects.filter(email=email)
# 		if user_qs.exists():
# 			raise ValidationError('User already exists')
# 		return value 


# 	def validate_email2(self, value):                              
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		return value 


# 	def create(self, validated_data):                                
# 		# print(validated_data)
# 		username = validated_data['username']
# 		email = validated_data['email']
# 		password = validated_data['password']
# 		user_obj = User(
# 			username = username,
# 			email=email
# 		)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data


# class UserLoginSerializer(ModelSerializer):
# 	# password2 = PasswordField()
# 	token = CharField(allow_blank=True, read_only=True)
# 	username = CharField(required=False, allow_blank=True)
# 	email = EmailField(label='Email Adress', required=False, allow_blank=True)
	
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'password',
# 			'token'
# 			# 'password2',
# 		]

# 		extra_kwargs = {"password":                                  
# 							{"write_only": True}
# 				}

# 	def validate(self, data):
# 		user_obj = None
# 		email = data.get('email', None)
# 		username = data.get('username', None)
# 		password=data["password"]
# 		if not username and not email:
# 			raise ValidationError("Username or email required  to login")

# 		user = User.objects.filter(
# 			Q(email=email) |
# 			Q(username=username)
# 		).distinct()
# 		user = user.exclude(email__isnull=True).exclude(email__iexact="")
# 		if user.exists() and user.count() == 1:
# 			user_obj = user.first()
# 		else:
# 			raise ValidationError("This username/email is not valid")

# 		if user_obj:
# 			if not user_obj.check_password(password):
# 				raise ValidationError('Inncorrect credentials')

# 		data["token"] = "SOME RANDOM TOKEN"

# 		return data


# 		# user_qs = User.objects.filter(email=email)
# 		# if user_qs.exists():
# 		# 	raise ValidationError('User already exists')

		



# # NOTES !!!!!!!!!!!!!!!!!!
# # we can go to localhost:8000/api/users/login/  ... user can login with email/username and password 












# # LOGIC .... USER API SETUP 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField   # added emailfield              

# from social.models import Post, Comment, User                                    
# from members.models import User

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class UserCreateSerializer(ModelSerializer):
# 	# password2 = PasswordField()
# 	email = EmailField(label='Email Adress')
# 	email2 = EmailField(label='Confirm Email')
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'email2',
# 			'password'
# 			# 'password2',
# 		]

# 		extra_kwargs = {"password":                                 # this is to hide password from displaying in the api interface 
# 							{"write_only": True}
# 				}

# 	def validate(self, data):
# 		# email = data['email']
# 		# user_qs = User.objects.filter(email=email)
# 		# if user_qs.exists():
# 		# 	raise ValidationError('User already exists')

# 		return data


# 	def validate_email(self, value):                              # validating emails ... emails must match 
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		user_qs = User.objects.filter(email=email)
# 		if user_qs.exists():
# 			raise ValidationError('User already exists')
# 		return value 


# 	def validate_email2(self, value):                              # validating emails ... emails must match 
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		return value 


# 	def create(self, validated_data):                                # this function will create our user using the api interface 
# 		# print(validated_data)
# 		username = validated_data['username']
# 		email = validated_data['email']
# 		password = validated_data['password']
# 		user_obj = User(
# 			username = username,
# 			email=email
# 		)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data



# # NOTES !!!!!!!!!!!!!!!!!!11
# # localhost:8000/api/users/register            ..... successfully can reguster user 





















# # LOGIC .... Base apiview for user login 

# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField # charfield                

# from social.models import Post, Comment, User                                    
# from members.models import User

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import get_user_model

# from django.db.models import Q              # added q 


# User = get_user_model()

# class UserCreateSerializer(ModelSerializer):
# 	# password2 = PasswordField()
# 	email = EmailField(label='Email Adress')
# 	email2 = EmailField(label='Confirm Email')
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'email2',
# 			'password'
# 			# 'password2',
# 		]

# 		extra_kwargs = {"password":                                  
# 							{"write_only": True}
# 				}

# 	def validate(self, data):
# 		# email = data['email']
# 		# user_qs = User.objects.filter(email=email)
# 		# if user_qs.exists():
# 		# 	raise ValidationError('User already exists')

# 		return data


# 	def validate_email(self, value):                               
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		user_qs = User.objects.filter(email=email)
# 		if user_qs.exists():
# 			raise ValidationError('User already exists')
# 		return value 


# 	def validate_email2(self, value):                              
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match")
# 		return value 


# 	def create(self, validated_data):                                
# 		# print(validated_data)
# 		username = validated_data['username']
# 		email = validated_data['email']
# 		password = validated_data['password']
# 		user_obj = User(
# 			username = username,
# 			email=email
# 		)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data


# class UserLoginSerializer(ModelSerializer):
# 	# password2 = PasswordField()
# 	token = CharField(allow_blank=True, read_only=True)
# 	username = CharField(required=False, allow_blank=True)
# 	email = EmailField(label='Email Adress', required=False, allow_blank=True)
	
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'password',
# 			'token'
# 			# 'password2',
# 		]

# 		extra_kwargs = {"password":                                  
# 							{"write_only": True}
# 				}

# 	def validate(self, data):
# 		user_obj = None
# 		email = data.get('email', None)
# 		username = data.get('username', None)
# 		password=data["password"]
# 		if not username and not email:
# 			raise ValidationError("Username or email required  to login")

# 		user = User.objects.filter(
# 			Q(email=email) |
# 			Q(username=username)
# 		).distinct()
# 		user = user.exclude(email__isnull=True).exclude(email__iexact="")
# 		if user.exists() and user.count() == 1:
# 			user_obj = user.first()
# 		else:
# 			raise ValidationError("This username/email is not valid")

# 		if user_obj:
# 			if not user_obj.check_password(password):
# 				raise ValidationError('Inncorrect credentials')

# 		data["token"] = "SOME RANDOM TOKEN"

# 		return data


# 		# user_qs = User.objects.filter(email=email)
# 		# if user_qs.exists():
# 		# 	raise ValidationError('User already exists')

# 		return data



# # NOTES !!!!!!!!!!!!!!!!!!
# # we can go to localhost:8000/api/users/login/  ... user can login with email/username and password 