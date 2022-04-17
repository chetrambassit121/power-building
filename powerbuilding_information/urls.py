from django.urls import path                            # added path is used for routing URLs to the appropriate view functions within a Django application 
                                                		# https://www.fullstackpython.com/django-urls-path-examples.html
# from django.conf.urls import re_path                  # added 
from .views import HomeView                             # added ... importing the homeview function that we created in powerlifting_information/views.py file

# entire file was created by us 

urlpatterns = [
	path('', HomeView, name='home'),                    # using path function , '' empty string so it will be the landing page AKA home page, 
														# accessing HomeView, giving this path the name 'home' .. we can use the name to call the path when needed

]

