from django.shortcuts import render, get_object_or_404, redirect                                                    
from django.views import generic                            
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm                      
from django.contrib.auth.views import PasswordChangeView                                                                      
from django.urls import reverse_lazy                       
from .forms import SignUpForm, PasswordChangingForm, EditProfileForm, PasswordChangingForm, ProfilePageForm 
from django.views.generic import DetailView, CreateView, DeleteView, View                                                                  
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
from django.db import connection
from django.db.models import Q
# from validate_email import validate_email
                           
def register(request):
    if request.method == 'POST':
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
            email.send()
            return render(request, 'registration/confirm_email.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

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









# DATABASE ORM , SQL CODING !!!!!!!!!!!!!!!!
# ACCESS SQLITE EXPLORER .. right click dqsqlite3 .. click open database .. sqlite explorer will aviable for viewing 
# remove the _ at the end of the function to use it


# OVERVIEW 1 ... basic orm sql with django/python


# user sql view basic 
# def users_list(request):
def users_list_(request):    # added _ to halt this method 
    users = User.objects.all()   # variable users bound to all users with there fields 
    # users = User.objects.raw("SELECT * FROM members_user")     # sql way of getting all users with feilds 

    print(users)            # print users variable data into terminal
    print(users.query)      # print the users querys into terminal 
    print(connection.queries)    # sql connections query displayes time as well to load data 
    return render(request, 'registration/users_list.html', {'users': users})    # return html file with data 

# go to http://localhost:7000/members/users_list/ ..SQL info dispayed in template and SQL will be displayed in terminal 








# OVERVIEW 2 ... Simple object relational queries, simple OR query, Q objects - OR query, view query SQL, query performance 


# created another function .. # filtering user by first name ... doing two filter searches at once 
def users_list_(request):
    users = User.objects.filter(first_name__startswith='chetram') | User.objects.filter(first_name__startswith='john')
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display user information based on first_name .. on template and terminal 





# implemented Q for more advacbed search ... same as previous coding with less code ...  filtering user by first name ... doing two filter searches at once 
def users_list_(request):
    # users = User.objects.filter(Q(first_name__startswith='chetram') | Q(first_name__startswith='john'))
    users = User.objects.filter(~Q(first_name__startswith='chetram') | Q(first_name__startswith='john'))            # addded ~ to Q will halt that specfic Q search
    # users = User.objects.filter(Q(first_name__startswith='john'))                                                 # searching just for john first_name
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display user information based on first_name .. on template and terminal .. 
# we can keep adding new Q searches

# ...............................................................................................................






#OVERVIEW 3 ... Simple AND queries .. exclude ... simple AND query, Q objects-AND query, view query sql, query performance



# preform an AND query on database
def users_list_(request):
    users = User.objects.filter(city_id=1) & User.objects.filter(state_id=1)                                               
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display users information based on city_id and state_id .. both feilds must be TRUE
# used & to search two different feilds and once 


# preform an AND query WITH Q on database
def users_list_(request):
    users = User.objects.filter(Q(first_name__startswith='chetram') & Q(last_name__startswith='bassit'))                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ... will display users information based on specfic fields 
# used & to search two different feilds and once 



# using exclude with & and Q
def users_list_(request):
    users = User.objects.exclude(Q(first_name__startswith='chetram') & Q(last_name__startswith='bassit'))                                              
    # users = User.objects.exclude(city_id=1) & User.objects.filter(first_name__startswith='chetram')                                               
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})   

# go to http://localhost:7000/members/users_list/   ...returns all user but exclude users with the following fields .. 
# used exclude 

# ...........................................................................................








#OVERVIEW 4 ... Simple UNION queries ... Simple UNION query, view query sql, query performance
# usng the User model and the UserProfile model ... using UNION to acces data from both models 

# values_list and using UNION 
def users_list_(request):
    users = User.objects.all().values_list("first_name").union(UserProfile.objects.all().values_list("first_name"))                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})

# gets first name for both User model and UserProfile model ... if firstname is in both models it will only be displayed once
# so it also doesnt display duplicate fistnames 



# values and using UNION     .......   different from values_list .... return in dictionary form "value":"key"
def users_list_(request):
    users = User.objects.all().values("first_name").union(UserProfile.objects.all().values("first_name"))                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 


# ......................................................








#OVERVIEW 5 ... Simple NOT queries ... Simple NOT query, view query sql, query performance

# NOT Eexample in SQL lanuage 
# SELECT * FROM Users WHERE NOT first_name = chetram

# NOT Eexample in ORM lanuage 
# exclude()
# filter(~Q)


# using exclude 
def users_list_(request):
    users = User.objects.exclude(first_name__startswith='chetram')                                                                                      
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 



# using exclude with & .. excluding based on 2 parameters
def users_list_(request):
    users = User.objects.exclude(first_name__startswith='chetram') & User.objects.exclude(last_name__startswith='doe')                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 



# using parameters inside exclude ... WE DO NOT HAVE AN AGE FEILD USING AS AN EXMPLE CODING CANNOT EXECUTE UNTIL ADDING AGE FIELD TO MODELS
def users_list_(request):
    users = User.objects.exclude(age__gt=19)                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 

    # gt       GREATER THAN
    # gte      GREATER THAN OR EQUAL TO 
    # lt       LESS NOT 
    # lte      LESS THEN OR EQUAL TO 
# this func will return all user queryes excluding those greater than age 19



# using exclude wth Q and parameters
def users_list_(request):
    users = User.objects.exclude(~Q(age__gt=19))                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 
# this func will return all user queryes excluding those greater than age 19



# using exclude wth Q and parameters and & 
def users_list_(request):
    users = User.objects.exclude(~Q(age__gt=19)&~Q(first_name__Startswith='chetram'))                                                                              
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users}) 
# exclusing queries based on two feilds 

# .....................................................................









# OVERVIEW 6 ... Simple field selection and output ... selecting indiviusal database fields .. outputting to template


# using ONLY
def users_list_(request):
    users = User.objects.filter(city_id=1).only('first_name')                                                                  
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
    
# get user based on city and return users firstname 

# ......................................................................................








# OVERVIEW 7 .. performing RAW queries with SQL
# raw method takes a raw SQL query and executes them 



def users_list_(request):
    sql = "SELECT * FROM members_user"
    users = User.objects.raw(sql)            # select everything from members app, user model                                                       
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# will display all queries from that table members_user 



# elect everything from members app, user model, where the last name is doe 
def users_list_(request):
    users = User.objects.raw("SELECT * FROM members_user WHERE last_name='doe'")                                                          
    print(users)            
    print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# displays all data if last name is doe 



# 
def users_list(request):
    users = User.objects.all()
    for u in User.objects.raw("SELECT * FROM members_user"):
        print(u)

    # print(users)            
    # print(connection.queries)     
    return render(request, 'registration/users_list.html', {'users': users})
# .................................................




































