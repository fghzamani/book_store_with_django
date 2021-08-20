from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Discount
from .forms import CouponApplyForm


@require_POST
def discount_apply(request):
    
    print("request.method:",request.method)
    if request.method == 'POST':
        mycode = request.POST['discount']
        print('mycode',mycode)
        now = timezone.now()
        
        try:
            
            discount = Discount.objects.get(code__iexact=mycode,created_date__lte=now,expired_date__gte=now,active=True)
            request.session['discount_id'] = discount.id
            request.session['isvalid_discount'] = 1
            
        except Discount.DoesNotExist:
            request.session['discount_id'] = None
            request.session['isvalid_discount'] = -1

        return redirect('cart_detail')
