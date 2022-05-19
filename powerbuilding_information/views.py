from django.shortcuts import render, get_object_or_404      # Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
										                                        # https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render
from django.shortcuts import redirect                       # added redirect ... Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.
										                                        # https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import View
from .models import Survey
# Create your views here.


class HomeView(View):
  def get(self, request):                       # defining the homeview function .. this will literally be out home page 
  											                       # A django view is a python function which accept an argument called request and returns an response.
  	survey = Survey.objects.all()
  	return render(request, 'home.html', {'survey':survey})      # render gets an HTML template as a response .. we want to return this html template as the response 
  											                                        # https://www.geeksforgeeks.org/render-a-html-template-as-response-django-views/

def SurveyView(request):
  survey = Survey.objects.all()
  return render(request, 'surveys.html', {'survey':survey})

class AboutView(View):
  def get(self, request):
    return render(request, 'about.html')


def Powerlifting(request):
  return render(request, 'powerlifting.html')

def Bodybuilding(request):
  return render(request, 'bodybuilding.html')

def Powerbuilding(request):
  return render(request, 'powerbuilding.html')  


# @login_required
def like(request, id):
  user=request.user
  Likes=False
  Dislikes=False
  if request.method=="POST":
    survey_id=request.POST['survey_id']
    get_video=get_object_or_404(Survey, id=survey_id)

    if user in get_video.likes.all():
      get_video.likes.remove(user)
      Likes=False
      # get_video.save()
    elif user in get_video.dislikes.all():                                                      
      get_video.dislikes.remove(user) 
      Dislikes=False  
      # get_video.save()                                          
      get_video.likes.add(user)  
      Likes=True  
      # get_video.save()

    else:
      get_video.likes.add(user)
      Likes=True
      # get_video.save()

    data={
      "liked":Likes,
      "likes_count":get_video.likes.all().count(),
      "disliked":Dislikes,
      "dislikes_count":get_video.dislikes.all().count()
    }

    return JsonResponse(data, safe=False)
  return redirect(reverse("surveys", args=[str(id)]))


# @login_required
def dislike(request, id):
  user=request.user
  Dislikes=False
  Likes=False
  if request.method == "POST":
    survey_id=request.POST['survey_id']
    # print("printing ajax id", video_id)
    watch=get_object_or_404(Survey, id=survey_id)

    if user in watch.dislikes.all():
      watch.dislikes.remove(user)
      Dislikes = False
      # watch.save()

    elif user in watch.likes.all():
      watch.likes.remove(user)
      Likes=False
      # watch.save()
      watch.dislikes.add(user)                       
      Dislikes=True  
      # watch.save()
        
    else:                                                                               
      watch.dislikes.add(user)                                                            
      Dislikes=True  
      # watch.save()


    data={           
      "liked":Likes,
      "likes_count":watch.likes.all().count(),         
      "disliked":Dislikes,
      "dislikes_count":watch.dislikes.all().count()
    }
  
    return JsonResponse(data, safe=False)
  return redirect(reverse("surveys", args=[str(id)]))
