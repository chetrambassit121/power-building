from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from members.models import User

# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='powerbuilding_information' manage.py test && coverage report && coverage html 


class HomeHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<h1 style="display: none;">Homepage</h1>')
        self.assertNotContains(response, "Not on the page")

class AboutHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Content coming soon</h1>")
        self.assertNotContains(response, "Not on the page")

class PowerbuildingHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/powerbuilding/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("powerbuilding"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("powerbuilding"))
        self.assertTemplateUsed(response, "powerbuilding.html")

    def test_template_content(self):
        response = self.client.get(reverse("powerbuilding"))
        self.assertContains(response, "<h2>Content coming soon</h2>")
        self.assertNotContains(response, "Not on the page")

class BodybuildingHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/bodybuilding/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("bodybuilding"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("bodybuilding"))
        self.assertTemplateUsed(response, "bodybuilding.html")

    def test_template_content(self):
        response = self.client.get(reverse("bodybuilding"))
        self.assertContains(response, "<h2>Content coming soon</h2>")
        self.assertNotContains(response, "Not on the page")

class PowerliftingHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/powerlifting/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("powerlifting"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("powerlifting"))
        self.assertTemplateUsed(response, "powerlifting.html")

    def test_template_content(self):
        response = self.client.get(reverse("powerlifting"))
        self.assertContains(response, "<h2>Content coming soon</h2>")
        self.assertNotContains(response, "Not on the page")

class SurveyHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/surveys/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("surveys"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("surveys"))
        self.assertTemplateUsed(response, "surveys.html")

    def test_template_content(self):
        response = self.client.get(reverse("surveys"))
        self.assertContains(response, '<h1 style="display: none;">testing</h1>')
        self.assertNotContains(response, "Not on the page")































# class BaseTest(TestCase):                                        
# 	def setUp(self):
# 		self.home_url=reverse('home')
# 		self.about_url=reverse('about')
# 		self.survey_url=reverse('surveys')
# 		self.powerlifting_url=reverse('powerlifting')
# 		self.powerbuilding_url=reverse('powerbuilding')
# 		self.bodybuilding_url=reverse('bodybuilding')
# 		return super().setUp()

# class HtmlTest(BaseTest):
#     def test_can_access_home_page(self):
#         response=self.client.get(self.home_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'home.html')

#     def test_can_access_about_page(self):
#         response=self.client.get(self.about_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'about.html')

#     def test_can_access_survey_page(self):
#         response=self.client.get(self.survey_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'surveys.html')

#     def test_can_access_powerlifting_page(self):
#         response=self.client.get(self.powerlifting_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'powerlifting.html')

#     def test_can_access_powerbuilding_page(self):
#         response=self.client.get(self.powerbuilding_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'powerbuilding.html')

#     def test_can_access_bodybuilding_page(self):
#         response=self.client.get(self.bodybuilding_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'bodybuilding.html')





















# ## testing with pytest 
# ## pytest test command .... pytest

# from django import urls
# from django.contrib.auth import get_user_model
# import pytest



# # pytest commands .... pytest 

# pytestmark = pytest.mark.django_db

# @pytest.mark.parametrize('param', [
# 	('home'),
# 	('about'),
# 	('home'),
# 	('surveys'),
# 	('powerbuilding'),
# 	('bodybuilding'),
# 	('powerlifting')

# ])
# def test_render_views(client, param):
# 	temp_url = urls.reverse(param)
# 	resp = client.get(temp_url)
# 	assert resp.status_code == 200