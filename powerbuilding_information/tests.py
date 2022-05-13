from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):                                        # testing for homepage response .. 
	def test_testhomepage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)              # using assertequals to check if the respose statuscode matchs the 200 status code
																 # basically we want the responses status code to be 200 ... if not then error of 404 automatically 




# COMMAND TERMINAL TESTING COMMANDS
#  
# run all tests .... python manage.py test .... this will run ALL tests in project 
# run all test in a specfic app .... python manage.py test powerbuilding_information  
# run a specfic testing class in a specfic app ... python manage.py test powerbuilding_information.tests.URLTests
# run a specfic method in a specfic testing class in a specfic app ... python manage.py test powerbuilding_information.tests.URLTests.test_testhomepage 

# when we run this specfic test to see if '/' the homepage returns with a status of 200 we get ... 
# Ran 1 test in 1.694s

# OK
