from django import urls
from django.contrib.auth import get_user_model
import pytest
# from powerbuilding_information.views import HomeView


# python test command .... python manage.py test
# coverage command .... coverage run manage.py test
# coverage report command .... coverage report  
# coverage run --source='members' manage.py test && coverage report && coverage html 





# pytest 
pytestmark = pytest.mark.django_db

@pytest.mark.parametrize('param', [
	# ('home'),
	('login'),
	('register'),
])
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200


# @pytest.mark.django_db
# def test_user_signup(client, user_data):
# 	user_model = get_user_model()
# 	assert user_model.objects.count() == 0
# 	signup_url = urls.reverse('login')
# 	resp = client.post(signup_url, user_data)
# 	assert user_model.objects.count() == 1
# 	assert resp.status_code == 302


# @pytest.mark.django_db
# def test_user_login(client, create_test_user, user_data):
# 	user_model = get_user_model()
# 	assert user_model.objects.count() == 1
# 	login_url = urls.reverse('login')
# 	resp = client.post(login_url, data=user_data)
# 	assert resp.status_code == 302
# 	assert resp.url == urls.reverse('home')


# @pytest.mark.django_db
# def test_user_logout(client, authenticated_user):
# 	logout_url = urls.reverse('logout')
# 	resp = client.get(logout_url)
# 	assert resp.status_code == 302
# 	assert resp.url == urls.reverse('home')