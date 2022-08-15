from django import urls
from django.contrib.auth import get_user_model
import pytest


'''
python test command .... python manage.py test
coverage command .... coverage run manage.py test
coverage report command .... coverage report
coverage run --source='powerbuilding_information' manage.py test && coverage report && coverage html
'''

pytestmark = pytest.mark.django_db

@pytest.mark.parametrize('param', [
	('home'),
	('about'),
	('home'),
	('surveys'),
	('powerbuilding'),
	('bodybuilding'),
	('powerlifting')

])
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200
