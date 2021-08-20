from django.shortcuts import render,redirect,reverse
from cart.cart import Cart
from .models import Orderdetail,Order
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from users.models import Customer


def order_create(request):
    cart = Cart(request)
    print('Type cart',type(cart))
    print('request:',request.method)
    if request.method == 'GET':
        customer = Customer.objects.all()[0]
        if len(cart) != 0:
            if cart.discount:
                
                discount = cart.discount
                
                order = Order.objects.create(customer = customer,discount=discount,billing_address=customer.address,
                total_price= cart.get_total_price_after_discount())
                
            
            else:
                order = Order.objects.create(customer = customer,billing_address=customer.address,
                total_price= cart.get_total_price_after_discount()) 
                            
            for item in cart:
                Orderdetail.objects.create(order=order,book=item['book'],unit_price=item['price'],quantity=item['quantity'])
                
            
            order.state =True
            order.save()
        
        request.session['discount_id']=0
        cart.clear() # clear the cart
        
        request.session['order_id'] = order.id  # set the order in the session
        
        # a = Order.objects.filter(total_price__lte =0)
        # a.delete()
        
        return render(request,'orders/order_create.html',{'cart': cart})
    
   
    
        
def created_order(request ):
    return render(request , 'orders/order_created.html',{})

# @staff_member_required
# def admin_order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request,'admin/orders/order/detail.html',{'order': order})
