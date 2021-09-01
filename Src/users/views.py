from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm,UserProfileInfo,AddUserAddresForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User,Customer,Address
from django.contrib.auth.decorators import login_required
from orders.models import Order

def user_login(request):
   
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate( request, email =cd['email'], password=cd['password'])
			
			if user is not None:
				login(request, user)
				if request.user.is_staff==False:
					messages.success(request, 'شما با موفقیت وارد شدید', 'success')
					return redirect('dashboard')
				else:
					return redirect('staff_profile')
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
	if request.user.is_authenticated and request.user.is_staff==False:
		if request.method =='POST':
			user_form = UserProfileInfo( request.POST,instance=request.user)
			
			if user_form.is_valid():
				user_form.save()
				messages.success(request, 'اطلاعات شما با موفقیت ذخیره شد', 'success')
		user_form = UserProfileInfo(instance=request.user)
		return render(request,'users/userdashboard.html',{'user_form':user_form})
	elif request.user.is_staff==True:
		return redirect('staff_profile')
	return redirect('login')

@login_required
def add_new_address(request):
	if request.user.is_staff==False:
		addresses = {}
		try:
			# address = Address.objects.get(customer=request.user,is_default=True)
			addresses=Address.objects.filter(customer=request.user).exclude(is_active = False)
			print('addresses',addresses)
			if request.method =='POST':
				user_address = AddUserAddresForm(request.POST)
				if user_address.is_valid():
					cd=user_address.cleaned_data
					new_add = Address.objects.create(customer=request.user,address=cd['address'],postal_code=cd['postal_code'],city=cd['city'],is_default=cd['is_default'])
					new_add.save()
						
					messages.success(request,'آدرس جدید با موفقیت ذخیره شد','success')
			user_address = AddUserAddresForm()
		except:
			user_address = AddUserAddresForm()
		
		return render(request,'users/addaddress.html',{'user_address':user_address,'addresses':addresses})
	return redirect('/')

@login_required
def change_default_address(request):
	
	if request.method =="POST":
		choosen_address = request.POST.get("addr")
		result = Address.objects.get(id__exact=choosen_address)
		result.is_default=True
		result.save()
		other_add=Address.objects.filter(customer = request.user).exclude(id__exact=choosen_address)
		for ad in other_add:
			ad.is_default =False
			ad.save()

	return redirect('user addresses')

@login_required
def remove_address(request,address_id):
	"""
	remove user address in his/her profile 

	"""
	if request.user.is_staff==False:
		num_address = Address.objects.filter(customer = request.user).exclude(is_active = False).count()
		print('num add',num_address)
		if num_address >1 :
			address = get_object_or_404(Address, id=address_id)
			address.is_active = False
			address.save()
		return redirect('user addresses')
 

@login_required
def user_order_history(request):
	"""
	shows the user order history in user dashboard

	"""
	if request.user.is_staff==False:
		ordr_hist = Order.objects.filter(customer=request.user)
		return render(request,'users/order_history.html',{'ordr_hist':ordr_hist})

@login_required
def user_update_info(request):
	"""
	user can change some of his/her personal info

	"""
	if request.user.is_staff==False:
		if request.method =='POST':
			
			user_form = UserProfileInfo( request.POST,instance=request.user)
			if user_form.is_valid():
				user_form.save()
				messages.success(request, 'اطلاعات شما با موفقیت ذخیره شد', 'success')
		
		user_form = UserProfileInfo(instance=request.user)
		return render(request,'users/change_personalinfo.html',{'user_form':user_form})
	return redirect('/')
 