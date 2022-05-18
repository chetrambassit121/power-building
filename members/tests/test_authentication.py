# LOGIC ... testing register return status .. 

# from django.test import TestCase
# from django.urls import reverse 

# class BaseTest(TestCase):                                        
# 	def setUp(self):
# 		self.register_url=reverse('register')   
# 		return super().setUp()

# class RegisterTest(BaseTest):
# 	def test_can_view_page_correctly(self):
# 		response = self.client.get(self.register_url)
# 		self.assertEqual(response.status_code,200)
# 		self.assertTemplateUsed(response,'registration/register.html')



# to run this specfic test .... python manage.py test members.tests.test_authentication 
# testing to see if register returns with a status of 200 
# ..................................................................


















# 
# LOGIC ... testing the user data in register form 

# from django.test import TestCase
# from django.urls import reverse 

# class BaseTest(TestCase):                                        
# 	def setUp(self):
# 		self.register_url=reverse('register')   
# 		self.user={                                        # added the fields user enters in register form 
# 			'username': 'username',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'email': 'testemail@gmail.com',
# 			'password1': 'password1',
# 			'password2': 'password'
# 		}
# 		return super().setUp()

# class RegisterTest(BaseTest):
# 	def test_can_view_page_correctly(self):
# 		response = self.client.get(self.register_url)
# 		self.assertEqual(response.status_code,200)
# 		self.assertTemplateUsed(response,'registration/register.html')

# 	def test_can_register_user(self):                                        # added the method to see if user can register 
# 		response=self.client.post(self.register_url, self.user, format="text/html")
# 		self.assertEqual(response.status_code, 200)


# python manage.py test members.tests.test_authentication.RegisterTest.test_can_register_user to test new method 




















# # LOGIC ... testing the user password making sure its not too short 

# from django.test import TestCase
# from django.urls import reverse 

# class BaseTest(TestCase):                                        
# 	def setUp(self):
# 		self.register_url=reverse('register')   
# 		self.user={                                         
# 			'username': 'username',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'email': 'testemail@gmail.com',
# 			'password1': 'password1',
# 			'password2': 'password'
# 		}
# 		self.user_short_password={                            # added another variable and fields                         
# 			'username': 'username',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'email': 'testemail@gmail.com',
# 			'password1': 'tea',                             # made password only three charecters long to make is short 
# 			'password2': 'tea'
# 		}
# 		return super().setUp()

# class RegisterTest(BaseTest):
# 	def test_can_view_page_correctly(self):
# 		response = self.client.get(self.register_url)
# 		self.assertEqual(response.status_code,200)
# 		self.assertTemplateUsed(response,'registration/register.html')

# 	def test_can_register_user(self):                                        
# 		response=self.client.post(self.register_url, self.user, format="text/html")
# 		self.assertEqual(response.status_code, 200)

# 	def test_cant_register_user_withshortpassword(self):          # added method for short password testing                                
# 		response=self.client.post(self.register_url, self.user_short_password, format="text/html")
# 		self.assertEqual(response.status_code, 200)



# # 




















# LOGIC ... testing the user password1 == password 2  

# from django.test import TestCase
# from django.urls import reverse 

# class BaseTest(TestCase):                                        
# 	def setUp(self):
# 		self.register_url=reverse('register')   
# 		self.user={                                         
# 			'username': 'username',
# 			'email': 'testemail@gmail.com',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'password1': 'password1',
# 			'password2': 'password'
# 		}
# 		self.user_short_password={                                                   
# 			'username': 'username',
# 			'email': 'testemail@gmail.com',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'password1': 'tea',                            
# 			'password2': 'tea'
# 		}
# 		self.user_unmatching_password={                   # added to test if password 1 == password 2                                      
# 			'username': 'username',
# 			'email': 'testemail@gmail.com',
# 			'first_name': 'first_name',
# 			'last_name': 'last_name',
# 			'password1': 'teateas',                       # password have different values 
# 			'password2': 'teatea'
# 		}
# 		self.user_invalid_email={
#             'email':'test.com',
#             'username':'username',
#             'password':'teslatt',
#             'password2':'teslatto',
#             'name':'fullname'
#         }
# 		return super().setUp()

# class RegisterTest(BaseTest):
#     def test_can_view_page_correctly(self):
#        response=self.client.get(self.register_url)
#        self.assertEqual(response.status_code,200)
#        self.assertTemplateUsed(response,'registration/register.html')

#     def test_can_register_user(self):
#         response=self.client.post(self.register_url,self.user,format='text/html')
#         self.assertEqual(response.status_code,400)

#     def test_cant_register_user_withshortpassword(self):
#         response=self.client.post(self.register_url,self.user_short_password,format='text/html')
#         self.assertEqual(response.status_code,400)

#     def test_cant_register_user_with_unmatching_passwords(self):
#         response=self.client.post(self.register_url,self.user_unmatching_password,format='text/html')
#         self.assertEqual(response.status_code,400)

#     def test_cant_register_user_with_invalid_email(self):
#         response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
#         self.assertEqual(response.status_code,400)

#     def test_cant_register_user_with_taken_email(self):
#         self.client.post(self.register_url,self.user,format='text/html')
#         response=self.client.post(self.register_url,self.user,format='text/html')
#         self.assertEqual(response.status_code,400)























from django.test import TestCase
from django.urls import reverse 
from members.models import User

# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from authentication.utils import generate_token
from members.tokens import account_activation_token

# class SignUpPageTests(TestCase):
#     def setUp(self) -> None:
#         self.username = 'testuser'
#         self.email = 'testuser@email.com'
#         # self.age = 20
#         self.first_name = 'chetram'
#         self.last_name = 'bassit'
#         self.state = 'New York'
#         self.city = 'South Richmond Hill'
#         self.password = 'blacksam101'
#         self.password2 = 'blacksam101'

# #     def test_signup_page_url(self):
# #         response = self.client.get("/members/register/")
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, template_name='registration/register.html')

#     def test_signup_page_view_name(self):
#         response = self.client.get(reverse('register'))
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='registration/register.html')

# #     def test_signup_form(self):
# #         response = self.client.post(reverse('register'), data={
# #             'username': self.username,
# #             'email': self.email,
# #             # 'age': self.age,
# #             'first_name': self.first_name,
# #             'last_name': self.last_name,
# #             'state': self.state,
# #             'city': self.city,
# #             'password1': self.password,
# #             'password2': self.password
# #         })
# #         self.assertEqual(response.status_code, 200)

# #         users = get_user_model().objects.all()
# #         self.assertEqual(users.count(), 1)

class BaseTest(TestCase):                                        
	def setUp(self):
		# #register
		# self.user = {
		self.register_url=reverse('register')
		# self.user_profile_url=reverse('show_profile_page')      
		# self.username = 'testuser'
		# self.email = 'testuser@email.com'
  #       # self.age = 20
		# self.first_name = 'chetram'
		# self.last_name = 'bassit'
		# self.state = 'New York'
		# self.city = 'South Richmond Hill'
		# self.password = 'blacksam101'
		# }
		self.user={                                         
			'username': 'username',
			'email': 'nyforchoice@gmail.com',
			'first_name': 'chetty',
			'last_name': 'bassit',
			'state': 'New York',
			'city': 'South Richmond Hill',
			'password1': 'blacksam101',
			'password2': 'blacksam101'
		}
		self.user_short_password={                                                   
			'username': 'username',
			'email': 'testemail@gmail.com',
			'first_name': 'first_name',
			'last_name': 'last_name',
			'password1': 'tea',                            
			'password2': 'tea'
		}
		self.user_unmatching_password={                                                        
			'username': 'username',
			'email': 'testemail@gmail.com',
			'first_name': 'first_name',
			'last_name': 'last_name',
			'password1': 'teateas',                       
			'password2': 'teatea'
		}
		self.user_invalid_email={
            'email':'test.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
            'name':'fullname'
        }

        # login
		self.login_url=reverse('login')
		return super().setUp()

class RegisterTest(BaseTest):
	# REGISTER TESTING

	# self.register_url
    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/register.html')

    # self.user
    # def test_can_register_user(self):
    #     response=self.client.post(self.register_url,self.user,format='text/html')
    #     self.assertEqual(response.status_code,302)

 #    # self.user_short_password
 #    def test_cant_register_user_withshortpassword(self):
 #        response=self.client.post(self.register_url,self.user_short_password,format='text/html')
 #        self.assertEqual(response.status_code,400)

 #    # self.user_unmatching_password
 #    def test_cant_register_user_with_unmatching_passwords(self):
 #        response=self.client.post(self.register_url,self.user_unmatching_password,format='text/html')
 #        self.assertEqual(response.status_code,400)

	# # self.user_invalid_email
 #    def test_cant_register_user_with_invalid_email(self):
 #        response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
 #        self.assertEqual(response.status_code,400)

 #    # self.user
 #    def test_cant_register_user_with_taken_email(self):
 #        self.client.post(self.register_url,self.user,format='text/html')
 #        response=self.client.post(self.register_url,self.user,format='text/html')
 #        self.assertEqual(response.status_code,400)



# LOGIN TESTING
class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/login.html')
    # def test_login_success(self):
    #     self.client.post(self.register_url,self.user,format='text/html')
    #     user=User.objects.filter(username=self.user['username']).first()
    #     user.is_active=True
    #     user.save()
    #     response= self.client.post(self.login_url,self.user,format='text/html')
    #     self.assertEqual(response.status_code,302)
#     def test_cantlogin_with_unverified_email(self):
#         self.client.post(self.register_url,self.user,format='text/html')
#         response= self.client.post(self.login_url,self.user,format='text/html')
#         self.assertEqual(response.status_code,401)

#     def test_cantlogin_with_no_username(self):
#         response= self.client.post(self.login_url,{'password':'password','username':''},format='text/html')
#         self.assertEqual(response.status_code,401)
#     def test_cantlogin_with_no_password(self):
#         response= self.client.post(self.login_url,{'username':'password','password':''},format='text/html')
#         self.assertEqual(response.status_code,401)


# class HtmlTest(BaseTest):
#     def test_can_access_page(self):
#         response=self.client.get(self.user_profile_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'registration/user_profile.html')
