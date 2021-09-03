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
    """
    overriding Mixin for checking whether the client is customer or steff or superuser 

    """
    def dispatch(self,request,*args,**kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),self.get_login_url(),self.get_redirect_field_name())
        if self.request.user.is_staff==False:
            return redirect('/')
        return super(UserAccessMixin,self).dispatch(request,*args,**kwargs)

class BookCreateView(UserAccessMixin,CreateView):
    """
    this class enable staff and admin to add book to store

    """
    model=Book
    raise_exception=True
    permission_required = []
    form_class = AddNewBook
    template_name='profiles/add_new_book.html'
    # fields = ['title','author','price','inventory','cover','description','category','publisher']
    def get_success_url(self):
        return reverse('staff_profile')

class BookUpdateView(UserAccessMixin,UpdateView):
    """Update book info 
    """
    model=Book
    raise_exception=True
    permission_required = []
    fields = ['title','author','price','inventory','cover','description','category','publisher','coupon']
    template_name = 'profiles/book_edit.html'
    def get_success_url(self):
        return reverse('staff_profile')

class BookDeleteView(UserAccessMixin,DeleteView):
    """
    delete book from store

    """
    model=Book
    permission_required = []
    template_name = 'profiles/book_delete.html'
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class BookListView(UserAccessMixin,ListView):
    """
    show all books of store in panel

    """
    model=Book
    template_name = 'profiles/books_list.html'
    permission_required = []
class NewCategoryView(UserAccessMixin,CreateView):
    """enable staff and addmin to add a new category
    """
    model=Category
    permission_required = []
    template_name = 'profiles/new_category.html'
    fields=['name','slug']
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class NewCouponView(UserAccessMixin,CreateView):
    """
    add new coupon

    """
    model = Discount
    permission_required = []
    template_name = 'profiles/add_new_coupon.html'
    fields=['code','amount','expired_date','active']
    def get_success_url(self):
        return reverse('staff_profile')
class CouponListView(UserAccessMixin,ListView):
    """
    show all coupons of store in panel

    """
    permission_required = []
    model = Discount
    template_name = 'profiles/allcoupons.html'
   

class StaffProfileView(UserAccessMixin,TemplateView):
    """
    show staff panel to staffs

    """
    permission_required = []
    model = Staff
    template_name='profiles/staffprofile_home.html'
    

    
class StoreReportAdmin(TemplateView):
    """
    provides some reports for addmin in addmin panel

    """
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
    """
    enable addmin to add new staff to store

    """
    model=Staff
    raise_exception=True
    permission_required = ['staff.add_staff']
    template_name='profiles/addstaff.html'
    fields = ['email','password','first_name','last_name','username','is_staff']
    def get_success_url(self):
        return reverse('staff_profile')
