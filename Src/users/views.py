from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm,UserProfileInfo,AddUserAddresForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User,Customer,Address
from django.contrib.auth.decorators import login_required

def user_login(request):
   
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate( request, email =cd['email'], password=cd['password'])
			
			if user is not None:
				login(request, user)
				messages.success(request, 'شما با موفقیت وارد شدید', 'success')
				return redirect('index')
			else:
				messages.error(request, 'نام کاربری یا رمز عبور اشتباه است', 'danger')
				
	else:
		form = UserLoginForm()      
	return render(request, 'users/login.html', {'form':form})


def user_logout(request):
	logout(request)
	messages.success(request, 'you logged out successfully', 'success')
	return redirect('index')


def user_register(request):
    
	if request.method == 'POST':
		
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(first_name =cd['first_name'], last_name = cd['last_name']
			,password = cd['password'],email = cd['email'],username = cd['email'])
			user.save()
			login(request, user)
			messages.success(request, 'you registered successfully', 'success')
			return redirect('index')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/registration.html', {'form':form})


def user_dasshboard(request):
	"""
	if the user is sign in, shows his/her dashboard,else redirect the user to login page 
	"""
	if request.user.is_authenticated:
		if request.method =='POST':
			user_form = UserProfileInfo( request.POST,instance=request.user)
			
			if user_form.is_valid():
				user_form.save()
				messages.success(request, 'اطلاعات شما با موفقیت ذخیره شد', 'success')
		user_form = UserProfileInfo(instance=request.user)
		return render(request,'users/userdashboard.html',{'user_form':user_form})
	return redirect('login')

@login_required
def add_new_address(request):

	addresses = Address.objects.get(customer=request.user,is_default=True)
	if request.method =='POST':
		user_address = AddUserAddresForm(request.POST)
		if user_address.is_valid():
			cd=user_address.cleaned_data
			Address.objects.create(address=cd['address'],city=cd['city'],postal_code=cd['postal_code'],customer=request.user)
			messages.success(request,'آدرس جدید با موفقیت ذخیره شد','success')
	user_address = AddUserAddresForm()
	
	return render(request,'users/addaddress.html',{'user_address':user_address,'addresses':addresses})

@login_required
def user_order_history(request):
	"""
	shows the user order history in user dashboard

	"""
	if request.user.is_authenticated:
		return render(request,'users/order_history.html',{})

 