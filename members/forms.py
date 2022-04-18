from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                                                                
# from django.contrib.auth.models import User                             
from django import forms 
from .models import UserProfile, User, State, City

from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):              
	                              
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  
	
	class Meta:                                                                                         
		model = User                                                                                      
		fields = ('username', 'email', 'first_name', 'last_name', 'state', 'city', 'password1', 'password2')  

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
		    raise forms.ValidationError('Email already used')
		return email

	def __init__(self, *args, **kwargs):                                    
		super(SignUpForm, self).__init__(*args, **kwargs)                    
		self.fields['username'].widget.attrs['class'] = 'form-control'
		# self.fields['email'].widget.attrs['class'] = 'form-control'              
		self.fields['password1'].widget.attrs['class'] = 'form-control'      
		self.fields['password2'].widget.attrs['class'] = 'form-control'   
		self.fields['city'].queryset = City.objects.none()
		# self.fields['branch'].queryset = Branch.objects.none()

		if 'state' in self.data:
			try:
				state_id = int(self.data.get('state'))
				self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

