from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from members.models import User

class PostListHtmlUrlTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/social/post-list/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("post-list"))
        self.assertTemplateUsed(response, "social/post_list.html")

    def test_template_content(self):
        response = self.client.get(reverse("post-list"))
        self.assertContains(response, '<h1 style="display: none;">Socialpage</h1>')
        self.assertNotContains(response, "Not on the page")