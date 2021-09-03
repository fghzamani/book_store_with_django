from django import forms
from .models import User,Address,Customer
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email','password')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
			raise forms.ValidationError('passwords must match')
		return cd['password2']

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	"""
	form for password changing

	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('email', 'password', 'first_name','last_name')

	def clean_password(self):
		return self.initial['password']


class UserLoginForm(forms.Form):
	"""
	form used in login page

	"""
	email = forms.EmailField(label = 'ایمیل',widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(label = 'رمز عبور',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegistrationForm(forms.Form):
	"""
	[summary]

	"""
	email = forms.EmailField(label = 'ایمیل',widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(label = 'نام ',widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(label = 'نام خانوادگی',widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(label = 'رمز عبور',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
	class Meta:
		model = User
   

	def clean_email(self):
		'''
		Verify email is available.
		'''
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email


class UserProfileInfo(forms.ModelForm):
	"""
	form for showing customer info
	"""
	class Meta:
		model = Customer
		fields = ['first_name','last_name','email']

class AddUserAddresForm(forms.ModelForm):
	"""
	form for adding new address for customer

	"""
	class Meta:
		model = Address
		fields =['city','address','postal_code']


