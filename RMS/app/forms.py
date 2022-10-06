from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
class RegisterForm(UserCreationForm):
	password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'inp','placeholder':'Enter Your Password'}))
	password2=forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'inp','placeholder':'Enter Your Password Again'}))
	
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email'}
		widgets={'username':forms.TextInput(attrs={'class':'inp',
        'placeholder':'Enter Your UserName'}),
		'first_name':forms.TextInput(attrs={'class':'inp',
 		'placeholder':'First Name'}),
 		'last_name':forms.TextInput(attrs={'class':'inp',
 		'placeholder':'Last Name'}),
 		
 		'email':forms.EmailInput(attrs={'class':'inp','placeholder':'Enter Your Email'}),
 		}

class MyPasswordChangeForm(PasswordChangeForm):
	 def __init__(self, *args, **kwargs):
	 	super().__init__(*args, **kwargs)
	 	self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "inp"})
	 	self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "inp"})
	 	self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "inp"})