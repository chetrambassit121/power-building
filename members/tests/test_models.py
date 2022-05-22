from django.test import TestCase
from django.urls import reverse 
from members.models import User, MyAccountManager, State, City, UserProfile, BroadCast_Email
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from model_bakery import baker

# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='members' manage.py test && coverage report && coverage html 


# class TestMyAccountManager(TestCase):
# 	def test_email_error(self):
# 		user = MyAccountManager.create_user(email='', username='testuser', password='abc123')
# 		self.assertFormError(user, ValueError('Users must have an email'))

class BaseTest(TestCase):                                        
	def setUp(self):
		self.state = State.objects.create(name='New York')

		self.city = City.objects.create(state=self.state, name='Queens')

		# manually create user 
		self.user = User.objects.create(
			email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
			state=self.state, city=self.city, password='abc123'
		)
		
		# create user with baker w/ fields we want 
		self.user_baker = baker.make(User, username='testuser1', state=self.state, city=self.city)

		self.email = BroadCast_Email.objects.create(subject='testing', message='testing')	
		# self.userprofile = UserProfile.objects.create(user=self.user)

		return super().setUp()

class TestState(BaseTest):
	def test_state_str(self):
		# response=self.client.get(self.state)
		# state = State.objects.create(name='New York')
		state = self.state 
		self.assertEqual(str(state), 'New York')

class TestCity(BaseTest):
	def test_city_str(self):
		# state = State.objects.create(name='New York')
		# city = City.objects.create(state=state, name='Queens')
		city = self.city
		self.assertEqual(str(city), 'Queens')

class TestUser(BaseTest):
	def test_username_str(self):
		# state = State.objects.create(name='New York')
		# city = City.objects.create(state=state, name='Queens')
		# username = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
		# 						   state=state, city=city, password='abc123')
		username = self.user
		self.assertEqual(str(username), 'testuser')

class TestUserBaker(BaseTest):
	def test_username_str(self):
		# state = State.objects.create(name='New York')
		# city = City.objects.create(state=state, name='Queens')
		# username = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
		# 						   state=state, city=city, password='abc123')
		username = self.user_baker
		self.assertEqual(str(username), 'testuser1')

# class TestUserProfile(BaseTest):
# 	def test_user_str(self):
# 		# state = State.objects.create(name='New York')
# 		# city = City.objects.create(state=state, name='Queens')
# 		# username = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
# 		# 						   state=state, city=city, password='abc123')
# 		user_str = self.userprofile
# 		self.assertEqual(str(user_str), 'user')

class TestBroadcastEmail(BaseTest):
	def test_subject_str(self):
		subject = self.email
		self.assertEqual(str(subject), 'testing')










	# def test_has_perm(self):
	# 	state = State.objects.create(name='New York')
	# 	city = City.objects.create(state=state, name='Queens')
	# 	is_admin = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
	# 							   state=state, city=city, password='abc123', is_admin)
	# 	self.assertEqual(is_admin, False)

# class TestUserProfile(TestCase):
	# def test_user_str(self):
	# 	state = State.objects.create(name='New York')
	# 	city = City.objects.create(state=state, name='Queens')
	# 	create_user = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
	# 							   state=state, city=city, password='abc123')
	# 	user = UserProfile.objects.create(user=create_user)
	# 	self.assertEqual(user, create_user)

    # def test_get_absolute_url(self):
    #     state = State.objects.create(name='New York')
    #     city = City.objects.create(state=state, name='Queens')
    #     create_user = User.objects.create(email='test@gmail.com', username='testuser', first_name='chetram', last_name='bassit', 
				# 			   state=state, city=city, password='abc123')
    #     userprofile = UserProfile.objects.create()

    #     self.userprofile = UserProfile.objects.get(id=1)
    #     self.assertEqual("home", self.userprofile.get_absolute_url())