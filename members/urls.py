from django.urls import path         
from .views import register, RegistrationView, load_citys, PasswordsChangeView, ShowProfilePageView, ShowSharedProfilePageView, EditProfilePageView, UserEditView, UserDeleteView
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [

	#register urls 
    path('register/', views.register, name='register'),                         # url for register view .. user will be directed to register.html whih contains register form 
    # path('register/', RegistrationView.as_view(), name='register'),                         # url for register view .. user will be directed to register.html whih contains register form 

    path('ajax/load-citys/', views.load_citys, name='ajax_load_citys'),         # url which will load our dropdown dependent list which is in register form
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),        # url for the activation email sent to user 


	#password reset with user isnt logged in 
    path('reset_password/',
      auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),
      name="password_reset"),
    path('reset_password_sent/', 
      auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), 
      name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), 
      name="password_reset_confirm"),
    path('reset_password_complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
      name="password_reset_complete"),
   
    # changing password when user is logged in 
    path('<int:pk>/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name="change_password"), 
    path('password_success/', views.password_success, name='password_success'),  

    #user profile with posts
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),

    #user profile for shared posts
    path('<int:pk>/profile/shared/', ShowSharedProfilePageView.as_view(), name='show_shared_profile_page'),  

    # user edit profile page 
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),            

    # user edit settings 
    path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),                  

    # user delete 
    path('<int:pk>/delete/', UserDeleteView.as_view(template_name='registration/delete.html'), name="account_delete"),

]