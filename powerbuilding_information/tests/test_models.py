from powerbuilding_information.models import Survey
from members.models import User
# from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase, RequestFactory
import pytest
from members.models import User 
from powerbuilding_information.models import Survey 
from model_bakery import baker

# coverage
# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run manage.py test powerbuilding_information.tests.test_models && coverage report && coverage html
 





class BaseTest(TestCase):                                        
	def setUp(self):
		self.factory = RequestFactory()
		# self.testuser = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='abc123')
		self.testuser = baker.make(User)
		self.testuser2 = baker.make(User)
		# self.testuser2 = User.objects.create_user(username='testuser2', email='testuser2@gmail.com', password='abc123')
		self.survey = Survey.objects.create(question='test', extra_info="test")

		return super().setUp()



class TestSurveyModel(BaseTest):

	def test_survey_likes(self):
		self.survey.likes.set([self.testuser.pk, self.testuser2.pk])
		self.assertEqual(self.survey.likes.count(), 2)

	def test_survey_dislikes(self):
		self.survey.dislikes.set([self.testuser.pk, self.testuser2.pk])
		self.assertEqual(self.survey.dislikes.count(), 2)




























# from django.test import TestCase
# from powerbuilding_information.models import Survey

# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='powerbuilding_information' manage.py test && coverage report && coverage html 

# class TestAppModels(TestCase):

# 	def test_model_like(self):
# 		like = Survey.objects.create(likes=1)
# 		self.assertEqual(like)

# 	def test_model_dislike(self):
# 		dislike = Survey.objects.create(dislikes=1)
# 		self.assertEqual(dislike)












