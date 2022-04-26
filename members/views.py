from django.shortcuts import render, get_object_or_404, redirect                                                    
from django.views import generic                            
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm                      
from django.contrib.auth.views import PasswordChangeView                                                                      
from django.urls import reverse_lazy                       
from .forms import SignUpForm, PasswordChangingForm, EditProfileForm, PasswordChangingForm, ProfilePageForm 
from django.views.generic import DetailView, CreateView, DeleteView                                                                  
from .models import UserProfile, User, State, City
from social.models import Post                                                                                                                                                                
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from members.tokens import account_activation_token
from django.core import mail
from django.views.generic.list import ListView
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator   
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import json
                           

# Create your views here.
# def register(request):
#     if request.method=="POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         email = request.POST["email"]
#         state = request.POST["state"]
#         city = request.POST["city"]

#         user = User.objects.create_user(
#                 username = username,
#                 password = password,
#                 email = email,
#                 state = state,
#                 city = city
#             )
#         login(request.user)
#         subject = 'Activate your blog account'
#         message = render_to_string(
#                 'registration/email_template.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 }
#             )
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [user.email,]
#         send_mail(subject, message, email_from, recipient_list)
#         return render(request, 'registration/confirm_email.html') 
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    # connection = get_connection()
    # connection = mail.get_connection()
    # connection.open()
    if request.method == 'POST':
        # connection.open()
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string(
                'registration/email_template.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = mail.EmailMessage(mail_subject, message, to=[to_email])
            email.send_mail()
            # connection.close()
            return render(request, 'registration/confirm_email.html')  
            # connection.close()
            # return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

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



# loading the dependent dropdown for register form 
def load_citys(request):
    state_id = request.GET.get('state')
    citys = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'registration/city_dropdown_list_options.html', {'citys': citys})

# activation view for user to activate link to become user 
def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		# return HttpResponse('Thank you for your email confirmation. Now you can login account.')
		return render(request, 'registration/successful_registration.html') 
	else:
		return HttpResponse('Activation link is invalid!')    




# reset password while logged in 
class PasswordsChangeView(PasswordChangeView):                                                                           
    form_class = PasswordChangingForm                                           
    success_url = reverse_lazy('password_success')  

def password_success(request):                                                  
    return render(request, 'registration/password_success.html', {})  

 





# user profile 
class ShowProfilePageView(DetailView, ListView):    
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        followers = profile.followers.all()
        followings = profile.followings.all()
        p = Paginator(Post.objects.filter(author=user), 10)
        page = request.GET.get('page')
        posts = p.get_page(page)
        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        # if len(followings) == 0:
        #   is_follower = False

        # for following in followings:
        #   if following == request.user:
        #       is_follower = True
        #       break
        #   else:
        #       is_follower = False

        number_of_followings = len(followings)

            
        context = {
            'user': user,
           
            'profile': profile,
            'posts': posts,
            # 'following_count':following_count,
            # 'followers_count':followers_count,
            # 'follow_status':follow_status,
            # 'sharedposts': sharedposts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'number_of_followings': number_of_followings,
            # 'is_follower': is_follower,
        }

        return render(request, 'registration/user_profile.html', context)


class ShowSharedProfilePageView(DetailView):    
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user)
        sharedposts = Post.objects.filter(shared_user=user)
        followers = profile.followers.all()
        followings = profile.followings.all()

        p = Paginator(Post.objects.filter(shared_user=user), 10)
        page = request.GET.get('page')
        sharedposts = p.get_page(page)

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)


        if len(followings) == 0:
            is_follower = False

        for following in followings:
            if following == request.user:
                is_follower = True
                break
            else:
                is_follower = False

        number_of_followings = len(followings)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'sharedposts': sharedposts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'number_of_followings': number_of_followings,
            'is_follower': is_follower,
        }

        return render(request, 'registration/get_sharedposts_for_profilepage.html', context)


# edit profile page
class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'birth_date', 'location', 'bio', 'picture', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']
    template_name = 'registration/edit_profile_page.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('show_profile_page', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


# edit user settings 
class UserEditView(generic.UpdateView):                                             
    model = User
    form_class = EditProfileForm                                     
    template_name = 'registration/edit_profile.html'                                          

    def get_object(self):                                                           
        return self.request.user     

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('show_profile_page', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

#delete users account
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('login')
