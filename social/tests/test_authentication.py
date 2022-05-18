from django.test import TestCase
from django.urls import reverse 
from members.models import User

class BaseTest(TestCase):                                        
	def setUp(self):
		self.post_list_url=reverse('post-list')
		return super().setUp()

class HtmlTest(BaseTest):
    def test_can_view_page_correctly(self):
        response=self.client.get(self.post_list_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'social/post_list.html')
