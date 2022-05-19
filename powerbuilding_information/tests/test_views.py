# from django import urls
# from django.contrib.auth import get_user_model
# import pytest
# # from powerbuilding_information.views import HomeView


## pytest commands .... pytest 

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