from django.shortcuts import render       # Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
										  # https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render
from django.shortcuts import redirect     # added redirect ... Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.
										  # https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect
# Create your views here.


def HomeView(request):                       # defining the homeview function .. this will literally be out home page 
											 # A django view is a python function which accept an argument called request and returns an response.
	return render(request, 'home.html')      # render gets an HTML template as a response .. we want to return this html template as the response 
											 # https://www.geeksforgeeks.org/render-a-html-template-as-response-django-views/