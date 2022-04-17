# from django.shortcuts import render                                  # default 
# from django.shortcuts import render, get_object_or_404, redirect	 # added for returning files, objects, data 

# # from .models import UserProfile, User, State, City                   # added importing our created models 
# # from .forms import SignUpForm										 # importing signup form for register view 

# # from members.tokens import account_activation_token                  		# for register / activate view 
# # from django.core import mail                                                # for register view 
# # from django.template.loader import render_to_string                         # for register view 
# # from django.contrib.sites.shortcuts import get_current_site          		# for activate view
# # from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  # for activate view 
# # from django.http import HttpResponse                                        # for activate view 
# # from django.utils.encoding import force_bytes, force_str                  # for activate view 
# # from members.tokens import account_activation_token                         # for activate view 
# # from django.contrib.auth import login                                       # activate view 


# from .forms import SignUpForm
# # , EditProfileForm, PasswordChangingForm, ProfilePageForm
# # get_state_strings, get_city_strings         
# from django.views.generic import DetailView, CreateView, DeleteView                                                                  
# from .models import UserProfile, User, State, City
# # , Branch
# # from social.models import Post 
# # Follow                                                                                                                                                                         
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.http import HttpResponse
# from django.utils.encoding import force_bytes, force_str
# from members.tokens import account_activation_token
# from django.core import mail
# from django.views.generic.list import ListView
# # from django.contrib.auth.models import User
# # from members.models import User 

# # from django.utils.encoding import force_text
# from django.contrib.auth import login
# from django.core.mail import send_mail, BadHeaderError
# from django.template.loader import render_to_string
# from django.db.models.query_utils import Q
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# from django.core.paginator import Paginator   
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy, reverse
# # from django_conf import base 
# from powerbuilding.settings import base 
# import json
                           

## Create your views here.

# register view
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string(
#                 'registration/email_template.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 }
#             )
#             to_email = form.cleaned_data.get('email')
#             email = mail.EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return render(request, 'registration/confirm_email.html')  
#             # return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})

# def register(request):
#     if request.method=="POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate your blog account.'
#             message = render_to_string(
#                 'registration/email_template.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 }
#             )
#             email_from = base.EMAIL_HOST_USER
#             recipient_list = [user.email,]
#             send_mail(subject, message, email_from, recipient_list)
#             return render(request, 'registration/confirm_email.html')  
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})



#loading the dependent dropdown for register form 
# def load_citys(request):
#     state_id = request.GET.get('state')
#     citys = City.objects.filter(state_id=state_id).order_by('name')
#     return render(request, 'registration/city_dropdown_list_options.html', {'citys': citys})

# # activation view for user to activate link to become user 
# def activate(request, uidb64, token):
# 	try:
# 		uid = force_str(urlsafe_base64_decode(uidb64))
# 		user = User.objects.get(pk=uid)
# 	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
# 		user = None
# 	if user is not None and account_activation_token.check_token(user, token):
# 		user.is_active = True
# 		user.save()
# 		login(request, user)
# 		# return HttpResponse('Thank you for your email confirmation. Now you can login account.')
# 		return render(request, 'registration/successful_registration.html') 
# 	else:
# 		return HttpResponse('Activation link is invalid!')    