from django.test import TestCase
from django.urls import reverse 
from members.models import User

class BaseTest(TestCase):                                        
	def setUp(self):
		self.home_url=reverse('home')
		self.about_url=reverse('about')
		self.survey_url=reverse('surveys')
		self.powerlifting_url=reverse('powerlifting')
		self.powerbuilding_url=reverse('powerbuilding')
		self.bodybuilding_url=reverse('bodybuilding')
		return super().setUp()

class HtmlTest(BaseTest):
    def test_can_access_home_page(self):
        response=self.client.get(self.home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_can_access_about_page(self):
        response=self.client.get(self.about_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'about.html')

    def test_can_access_survey_page(self):
        response=self.client.get(self.survey_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'surveys.html')

    def test_can_access_powerlifting_page(self):
        response=self.client.get(self.powerlifting_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'powerlifting.html')

    def test_can_access_powerbuilding_page(self):
        response=self.client.get(self.powerbuilding_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'powerbuilding.html')

    def test_can_access_bodybuilding_page(self):
        response=self.client.get(self.bodybuilding_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'bodybuilding.html')
