from django.urls import (
    path,
)  

from .views import (
    AboutView,
    Bodybuilding,
    HomeView,
    # IndexView,
    Powerbuilding,
    Powerlifting,
    SurveyView,
    dislike,
    like,
    HomeTwoView
)

# https://www.fullstackpython.com/django-urls-path-examples.html
# entire file was created by us

urlpatterns = [
    path(
        "", HomeView.as_view(), name="home"
    ),  
    path(
        "hometwo/", HomeTwoView.as_view(), name="index"
    ),  
    path("like/<int:id>/", like, name="likes"),
    path("dislike/<int:id>/", dislike, name="dislikes"),
    path("surveys/", SurveyView, name="surveys"),
    path("about/", AboutView.as_view(), name="about"),
    path("powerlifting/", Powerlifting, name="powerlifting"),
    path("bodybuilding/", Bodybuilding, name="bodybuilding"),
    path("powerbuilding/", Powerbuilding, name="powerbuilding"),
]
