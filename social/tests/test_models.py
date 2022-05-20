from django import urls
from django.contrib.auth import get_user_model
from social.models import Post, PostTest
from members.models import User
# from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
import pytest

# coverage
# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='social' manage.py test && coverage report && coverage html 

class TestPostModel(TestCase):

	def test_post_body(self):
		bodytest = PostTest.objects.create(bodytest='django testing', slug="django testing")
		self.assertEqual(str(bodytest), 'django testing') 

	def test_post_likes(self):
		testuser = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='abc123')
		testuser2 = User.objects.create_user(username='testuser2', email='testuser2@gmail.com', password='abc123')
		post = PostTest.objects.create(bodytest='test', slug="test")
		post.likestest.set([testuser.pk, testuser2.pk])
		self.assertEqual(post.likestest.count(), 2)

	def test_post_dislikes(self):
		testuser = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='abc123')
		testuser2 = User.objects.create_user(username='testuser2', email='testuser2@gmail.com', password='abc123')
		post = PostTest.objects.create(bodytest='test', slug="test")
		post.dislikestest.set([testuser.pk, testuser2.pk])
		self.assertEqual(post.dislikestest.count(), 2)






# from django.test import TestCase
# from social.models import PostTest
# from members.models import User
# from model_bakery import baker
# from pprint import pprint


# class TestPostTestModel(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         print('db test')
#         # Set up data for the whole TestCase
#         testuser = User.objects.create_user(
#             username='testuser', email='testuser@gmail.com', password='abc123')
#         testuser2 = User.objects.create_user(
#             username='testuser2', email='testuser2@gmail.com', password='abc123')
#         cls.new = PostTest.objects.create(
#             new="django", slug="django")
#         cls.new.likestest.set([testuser.pk, testuser2.pk])
#         cls.new.dislikestest.set([testuser.pk, testuser2.pk])


#     def test_model_str1(self):
#         self.assertEqual(str(self.new), "django")

#     def test_post_has_an_author(self):
#         self.assertEqual(self.new.likestest.count(), 2)

#     def test_get_absolute_url(self):
#         self.new.slug = PostTest.objects.get(id=1)
#         self.assertEqual("/django/", self.new.slug.get_absolute_url())


# class TestPostTestNew(TestCase):

#     def setUp(self):
#         self.post = baker.make('social.PostTest')
#         pprint(self.post.__dict__)

#     def test_model_str(self):
#         bodytest = PostTest.objects.create(bodytest="Django Testing")
#         # content = PostTest.objects.create(content="This is some content")
#         self.assertEqual(str(bodytest), "Django Testing")
