from django.shortcuts import render
from django.views.generic import ListView,FormView, DetailView,CreateView,UpdateView , DeleteView,TemplateView
from users.models import Staff
from products.models import Book,Category
from .forms import AddNewBook
from django.urls import reverse_lazy,reverse
from discount.models import Discount
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from users.models import Staff ,Customer
from orders.models import Order
from django.db.models import Sum

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self,request,*args,**kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),self.get_login_url(),self.get_redirect_field_name())
        if self.request.user.is_staff==False:
            return redirect('/')
        return super(UserAccessMixin,self).dispatch(request,*args,**kwargs)

class BookCreateView(UserAccessMixin,CreateView):
    model=Book
    raise_exception=True
    permission_required = []
    form_class = AddNewBook
    template_name='profiles/add_new_book.html'
    # fields = ['title','author','price','inventory','cover','description','category','publisher']
    def get_success_url(self):
        return reverse('staff_profile')

class BookUpdateView(UserAccessMixin,UpdateView):
    model=Book
    raise_exception=True
    permission_required = []
    fields = ['title','author','price','inventory','cover','description','category','publisher']
    template_name = 'profiles/book_edit.html'
    def get_success_url(self):
        return reverse('staff_profile')

class BookDeleteView(UserAccessMixin,DeleteView):
    model=Book
    permission_required = []
    template_name = 'profiles/book_delete.html'
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class BookListView(UserAccessMixin,ListView):
    model=Book
    template_name = 'profiles/books_list.html'
    permission_required = []
class NewCategoryView(UserAccessMixin,CreateView):
    model=Category
    permission_required = []
    template_name = 'profiles/new_category.html'
    fields=['name','slug']
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class NewCouponView(UserAccessMixin,CreateView):
    model = Discount
    permission_required = []
    template_name = 'profiles/add_new_coupon.html'
    fields=['code','amount','expired_date','active']
    def get_success_url(self):
        return reverse('staff_profile')
class CouponListView(UserAccessMixin,ListView):
    permission_required = []
    model = Discount
    template_name = 'profiles/allcoupons.html'
   

class StaffProfileView(UserAccessMixin,TemplateView):
    permission_required = []
    model = Staff
    template_name='profiles/staffprofile_home.html'
    

    
class StoreReportAdmin(TemplateView):
    model = None
    template_name = 'profiles/adminreport.html'
    def dispatch(self,request,*args,**kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),self.get_login_url(),self.get_redirect_field_name())
        if self.request.user.is_superuser==False:
            return redirect('/')
        return super(StoreReportAdmin,self).dispatch(request,*args,**kwargs)
        
    def get_context_data(self,**kwargs):
        context = super(StoreReportAdmin,self).get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['orders'] = Order.objects.all()
        # context['incomes'] = Order.objects.filter().values('created_date').order_by('created_date').annotate(sum=Sum('total_price'))
        context['incomes'] = Order.objects.all().aggregate(sum=Sum('total_price'))
        context['order_num'] = Order.objects.all().count()
        context['customers_num'] = Customer.objects.filter(is_staff=False).count()
        return context
class NewStaffCreateView(UserAccessMixin,CreateView):
    model=Staff
    raise_exception=True
    permission_required = ['staff.add_staff']
    template_name='profiles/addstaff.html'
    fields = ['email','password','first_name','last_name','username','is_staff']
    def get_success_url(self):
        return reverse('staff_profile')
