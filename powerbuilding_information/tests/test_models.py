import pytest

from django.test import RequestFactory, SimpleTestCase, TestCase
from model_bakery import baker

from members.models import User
from powerbuilding_information.models import Survey

'''
coverage
python test command .... python manage.py test
coverage command .... coverage run manage.py test
coverage report command .... coverage report
coverage run manage.py test powerbuilding_information.tests.test_models && coverage report && coverage html
'''

class BaseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.testuser = baker.make(User)
        self.testuser2 = baker.make(User)
        self.survey = Survey.objects.create(question="test", extra_info="test")
        return super().setUp()


class TestSurveyModel(BaseTest):
    def test_survey_likes(self):
        self.survey.likes.set([self.testuser.pk, self.testuser2.pk])
        self.assertEqual(self.survey.likes.count(), 2)

    def test_survey_dislikes(self):
        self.survey.dislikes.set([self.testuser.pk, self.testuser2.pk])
        self.assertEqual(self.survey.dislikes.count(), 2)
