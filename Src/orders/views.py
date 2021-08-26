from django.shortcuts import render,redirect,reverse
from cart.cart import Cart
from .models import Orderdetail,Order
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from users.models import Customer ,Address
from django.contrib.auth.decorators import login_required

def order_create(request):
    """
    creating the orders and orderdetails instances

    """
    if request.user.is_authenticated:
        cart = Cart(request)
        
        if request.method == 'GET':
            customer = request.user
            customer_address = Address.objects.get(customer=request.user,is_default=True)
            print(customer_address)
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
                    
                
                order.state =True
                order.save()
            
            request.session['discount_id']=0
            cart.clear() # clear the cart
            
            request.session['order_id'] = order.id  # set the order in the session
            
            
            
            return render(request,'orders/order_create.html',{'cart': cart ,'customer_address':customer_address})
    return redirect('login')
    
   
    
@login_required(redirect_field_name='login')       
def created_order(request ):
    """
        if the order successfully sevedو this page will be rendered. it shows just a message  

    """
    return render(request , 'orders/order_created.html',{})

# @staff_member_required
# def admin_order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request,'admin/orders/order/detail.html',{'order': order})


