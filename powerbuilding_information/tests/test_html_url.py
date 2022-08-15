from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from members.models import User

'''
python test command .... python manage.py test
coverage command .... coverage run manage.py test
coverage report command .... coverage report
coverage run --source='powerbuilding_information' manage.py test && coverage report && coverage html
'''

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
