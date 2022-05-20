from powerbuilding_information.models import Survey
from members.models import User
# from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
import pytest
from members.models import User 
from powerbuilding_information.models import Survey 


# coverage
# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='social' manage.py test && coverage report && coverage html 


class TestSurveyModel(TestCase):

	def test_survey_likes(self):
		testuser = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='abc123')
		testuser2 = User.objects.create_user(username='testuser2', email='testuser2@gmail.com', password='abc123')
		survey = Survey.objects.create(question='test', extra_info="test")
		survey.likes.set([testuser.pk, testuser2.pk])
		self.assertEqual(survey.likes.count(), 2)

	def test_survey_dislikes(self):
		testuser = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='abc123')
		testuser2 = User.objects.create_user(username='testuser2', email='testuser2@gmail.com', password='abc123')
		survey = Survey.objects.create(question='test', extra_info="test")
		survey.dislikes.set([testuser.pk, testuser2.pk])
		self.assertEqual(survey.dislikes.count(), 2)




























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












