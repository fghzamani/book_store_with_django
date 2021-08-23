from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def user_login(request):
   
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate( request, email =cd['email'], password=cd['password'])
			print('user',user)
			print('emial',cd)
			
			if user is not None:
				login(request, user)
				messages.success(request, 'شما با موفقیت وارد شد', 'success')
				print("YESSSSSSSSSSSSS")
				return redirect('index')
			else:
				messages.error(request, 'نام کاربری یا رمز عبور اشتباه است', 'danger')
				print("YAYYYYYYYYYYYYYYYYYYYY")
	else:
		# messages.error(request,'Invalid username')
		form = UserLoginForm()      
	return render(request, 'users/login.html', {'form':form})


def user_logout(request):
	logout(request)
	messages.success(request, 'you logged out successfully', 'success')
	return redirect('index')


def user_register(request):
    
	if request.method == 'POST':
		print("REGISTERRRRRRRRRRRRRRRRRRRRRRR")
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print(cd)
			user = User.objects.create(first_name =cd['first_name'], last_name = cd['last_name']
			,password = cd['password'],email = cd['email'])
			print("REGISTERRRRRRRRRRRRRRRRRRRRRRR")
			user.save()
			login(request, user)
			messages.success(request, 'you registered successfully', 'success')
			return redirect('index')
	else:
		form = UserRegistrationForm()
		print("Whereeeeee")
	return render(request, 'users/registration.html', {'form':form})


