from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email','password1','password2']

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs={'class':'form-control'}
		self.fields['username'].label='UserName'
		self.fields['email'].widget.attrs={'class':'form-control'}
		self.fields['email'].label='Email'
		self.fields['password1'].widget.attrs={'class':'form-control'}
		self.fields['password1'].label='Password'
		self.fields['password2'].widget.attrs={'class':'form-control'}
		self.fields['password2'].label='Password Confirm'
class UserLoginForm(AuthenticationForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs={'class':'form-control'}
		self.fields['password'].widget.attrs={'class':'form-control'}


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email']

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs={'class':'form-control'}
		self.fields['username'].label='UserName'
		self.fields['email'].widget.attrs={'class':'form-control'}
		self.fields['email'].label='Email'
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['image'].widget.attrs={'class':'form-control-file'}
		self.fields['image'].label='Image'