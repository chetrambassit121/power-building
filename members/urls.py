from django.urls import path         
from .views import register, load_citys, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [

	#register urls 
    path('register/', views.register, name='register'),                         # url for register view .. user will be directed to register.html whih contains register form 
    path('ajax/load-citys/', views.load_citys, name='ajax_load_citys'),         # url which will load our dropdown dependent list which is in register form
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),        # url for the activation email sent to user 

	#password reset
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')), 
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
    path('password_success/', views.password_success, name='password_success'),  


     


]