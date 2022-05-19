from django import urls
from django.contrib.auth import get_user_model
import pytest
# from powerbuilding_information.views import HomeView


pytestmark = pytest.mark.django_db

@pytest.mark.parametrize('param', [
	('post-list'),
])
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200