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

from django.test import TestCase
from django.urls import reverse 

class BaseTest(TestCase):                                        
	def setUp(self):
		self.register_url=reverse('register')   
		self.user={                                         
			'username': 'username',
			'first_name': 'first_name',
			'last_name': 'last_name',
			'email': 'testemail@gmail.com',
			'password1': 'password1',
			'password2': 'password'
		}
		self.user_short_password={                                                   
			'username': 'username',
			'first_name': 'first_name',
			'last_name': 'last_name',
			'email': 'testemail@gmail.com',
			'password1': 'tea',                            
			'password2': 'tea'
		}
		self.user_unmatching_password={                   # added to test if password 1 == password 2                                      
			'username': 'username',
			'first_name': 'first_name',
			'last_name': 'last_name',
			'email': 'testemail@gmail.com',
			'password1': 'teateas',                       # password have different values 
			'password2': 'teatea'
		}
		self.user_invalid_email={
            
            'email':'test.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
            'name':'fullname'
        }
		return super().setUp()

class RegisterTest(BaseTest):
	def test_can_view_page_correctly(self):
		response = self.client.get(self.register_url)
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'registration/register.html')

	def test_can_register_user(self):                                        
		response=self.client.post(self.register_url, self.user, format="text/html")
		self.assertEqual(response.status_code, 200)

	def test_cant_register_user_withshortpassword(self):          # added method for short password testing                                
		response=self.client.post(self.register_url, self.user_short_password, format="text/html")
		self.assertEqual(response.status_code, 200)

	def test_cant_register_user_withunmatchingpasswords(self):          # added method for short password testing                                
		response=self.client.post(self.register_url, self.user_unmatching_password, format="text/html")
		self.assertEqual(response.status_code, 200)

	# def test_cant_register_user_with_invalid_email(self):
 #        response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
 #        self.assertEqual(response.status_code,400)

 #    def test_cant_register_user_with_taken_email(self):
 #        self.client.post(self.register_url,self.user,format='text/html')
 #        response=self.client.post(self.register_url,self.user,format='text/html')
 #        self.assertEqual(response.status_code,400)




# 


