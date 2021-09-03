from django.shortcuts import render,redirect,reverse
from cart.cart import Cart
from .models import Orderdetail,Order
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from users.models import Customer ,Address
from django.contrib.auth.decorators import login_required
from users.forms import  AddUserAddresForm

def order_create(request):
    """
    creating the orders and orderdetails instances

    """
   
    if request.user.is_authenticated and request.user.is_staff==False:
        cart = Cart(request)
        addresses=Address.objects.filter(customer=request.user).exclude(is_active = False)
        print("addresses",addresses)
        # if request.method =='POST':
        user_address = AddUserAddresForm(request.POST)
        
        if request.method == 'GET':
            customer = request.user
           
            customer_address = Address.objects.filter(customer=request.user).first()
            
            if len(cart) != 0:
                if cart.discount:
                    
                    discount = cart.discount
                    order = Order.objects.create(customer = customer,discount=discount,billing_address=customer_address,
                    total_price= cart.get_total_price_after_discount())
                    
                
                else:
                    order = Order.objects.create(customer = customer,billing_address=customer_address,
                    total_price= cart.get_total_price_after_discount()) 
                                
                for item in cart:
                    Orderdetail.objects.create(order=order,book=item['book'],unit_price=item['price'],quantity=item['quantity'])
                    item['book'].number_of_sell += item['quantity']
                    item['book'].save()
                    
                
                # order.state =True
                order.save()
            
            request.session['discount_id']=0
            cart.clear() # clear the cart
            
            # request.session['order_id'] = order.id  # set the order in the session
            
           
            return render(request,'orders/order_create.html',{'cart': cart ,'customer_address':customer_address ,'addresses':addresses})
    return redirect('login')

   
@login_required(redirect_field_name='login')       
def created_order(request ):
    """
        if the order successfully sevedو this page will be rendered. it shows just a message  

    """
    
    return render(request , 'orders/order_created.html',{})

@login_required
def process_order(request):
    if request.user.is_staff ==False:
        result = {}
        order = Order.objects.get(state=False , customer=request.user)
        if request.method =="POST":
            if request.POST.get("addr") != "new":
                choosen_address = request.POST.get("addr")
                print("CHOSEN ADD",choosen_address)
                result = Address.objects.get(id__exact=choosen_address)
                result.is_default=True
                order.billing_address = result
                order.state =True
                order.save()
                result.save()
            
            else:
                city = request.POST.get('state')  
                address = request.POST.get('address')
                postal_code = request.POST.get('code')
                result = Address.objects.create(customer=request.user,address=address,city = city,postal_code = postal_code , is_default=True)
                print(result)
                order.billing_address = result
                order.state =True
                order.save()
                result.save()
            other_add=Address.objects.exclude(id__exact=result.id)
            for ad in other_add:
                ad.is_default =False
                ad.save()
        
        return render(request,'orders/process.html',{'result':result})





# @staff_member_required 
# def admin_order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request,'admin/orders/order/detail.html',{'order': order})


