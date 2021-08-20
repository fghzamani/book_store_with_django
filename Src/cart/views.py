from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Book
from .cart import Cart
from .forms import CartAddProductForm 
from discount.forms import CouponApplyForm
from django.contrib import messages
from django.urls import reverse

@require_POST
def cart_add(request,book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        
        cd = form.cleaned_data
        if book.has_inventory(cd['quantity']):
            cart.add(book=book,
                        quantity=cd['quantity'],
                        override_quantity=cd['override'])
       
            return  redirect('cart_detail')
        
    
    return redirect('book_detail',pk = book.id)
    
@require_POST
def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)

    return redirect('cart_detail')


def cart_detail(request):
     
   
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    
    coupon_apply_form = CouponApplyForm()
    isvalid_discount = False
    
    a = 1
    if a == -1:
        isvalid_discount = True 
    else :
        isvalid_discount = False 

    return render(request, 'cart/cart_detail.html', {'cart': cart,'coupon_apply_form':coupon_apply_form, 'isvalid_discount':isvalid_discount})
