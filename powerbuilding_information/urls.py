from django.urls import path                            # added path is used for routing URLs to the appropriate view functions within a Django application 
                                                		# https://www.fullstackpython.com/django-urls-path-examples.html
# from django.conf.urls import re_path                  # added 
from .views import HomeView, like, dislike, SurveyView, AboutView, Powerlifting, Bodybuilding, Powerbuilding                  

# entire file was created by us 

urlpatterns = [
	path('', HomeView, name='home'),                    # using path function , '' empty string so it will be the landing page AKA home page, 
														# accessing HomeView, giving this path the name 'home' .. we can use the name to call the path when needed
	path("like/<int:id>/", like, name="likes"),
   	path("dislike/<int:id>/", dislike, name="dislikes"),
    path('surveys/', SurveyView, name='surveys'),
    path('about/', AboutView, name='about'),
    path('powerlifting/', Powerlifting, name='powerlifting'),
    path('bodybuilding/', Bodybuilding, name='bodybuilding'),
    path('powerbuilding/', Powerbuilding, name='powerbuilding'),






]

