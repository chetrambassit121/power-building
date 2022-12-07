"""powerbuilding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings  
from django.conf.urls.static import static 
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import include  
from django.urls import (
    path,
)  


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("powerbuilding_information.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
    path("social/", include("social.urls")),
    path("lists/", include("lists.urls")),
    # path("fitness/", include("fitness.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # path('api/auth/token/', obtain_jwt_token),
    path("api/social/", include("social.api.urls"), name="social-api"),
    path("api/users/", include("members.api.urls"), name="users-api"),
    path("__debug__/", include(debug_toolbar.urls)),
    # path(r'^api/social/', include("social.api.urls")),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  
