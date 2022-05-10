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
from django.contrib import admin
from django.urls import path                     # path is used for routing URLs to the appropriate view functions within a Django application
                                                 # https://www.fullstackpython.com/django-urls-path-examples.html
from django.urls import include                  # added 
from django.conf import settings                 # added
from django.conf.urls.static import static       # added
from django.contrib.auth import views as auth_views    # added 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('powerbuilding_information.urls')),    
    path('members/', include('django.contrib.auth.urls')),       
    path('members/', include('members.urls')),     
    path('social/', include('social.urls')),          
    path('ckeditor/', include('ckeditor_uploader.urls')),     

    path('api/social/', include("social.api.urls"), name='social-api'),
    # path(r'^api/social/', include("social.api.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            # added too access our media folder       
