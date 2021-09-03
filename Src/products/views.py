from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,FormView, DetailView,CreateView,UpdateView , DeleteView,TemplateView
from .models import Book,Category
from django.db.models import Q
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormMixin
# ,CartAddProductForm_func
class HomeView(TemplateView):
    """
        this class is for rendering main page(index) of site
    """
    model = Book
    template_name = 'bookshop/index.html' 
    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['newbook_list'] = Book.objects.all()[:4]
        context['best_seller'] = Book.objects.all().order_by('-number_of_sell')[:4]

        return context

   
    
    
class BookDetailView(DetailView): 
    """
    view the detail of every single book

    """
    model = Book
    template_name = 'bookshop/book_detail.html'
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # cartClass = CartAddProductForm_func(self.object.inventory)
        form_class = CartAddProductForm
        # context['form'] = cartClass(initial={'book': self.object})
        context['form'] = form_class(initial={'book': self.object})
        context['discount_price'] = self.object.get_discounted_price()
        if self.object.price == self.object.get_discounted_price():
            context['isDiscounted'] = False
        else:
            context['isDiscounted'] = True

        return context
  
    
    
    
class BookDetailForm_(FormView,FormMixin):
    """
    form for changing the number of 

    """
    template_name = 'bookshop/book_detail.html'
    form_class = CartAddProductForm
    # form_class = CartAddProductForm_func(5)
    success_url = '/cart/'


def BookDetailForm_func(max_inventory = 10):
    """
    rapper function [summary]

    """
    MAX_INVENTORY = max_inventory
    class BookDetailForm_(FormView,FormMixin):
        """
        form for changing the number of 

        """
        template_name = 'bookshop/book_detail.html'
        # form_class = CartAddProductForm
        form_class = CartAddProductForm_func(MAX_INVENTORY)
        success_url = '/cart/'
    
    return BookDetailForm_


class CategoryListView(ListView):
    """
    show lists of all categories

    """
    model = Category
    template_name = 'bookshop/all_category_list.html'
class CategoryDetailView(DetailView):
    """
    [summary]

    """
    model = Category
    template_name = 'bookshop/category_detail.html' 
  

class SearchList(ListView):
    """
    for searching and show results

    """
    model = Book
    template_name = 'bookshop/search.html'
    def get(self,request):
        """
        getting a string from searchbar and query through the database based on it

        """
        if request.method =="GET":
            search = request.GET.get('search')  
        if search:
            results = Book.objects.filter(
                Q(title__icontains=search)
                | Q(author__icontains=search)  # | is or
            )
            # distinct is used, otherwise same book will be listed
            # twice if book has two authors
            results = results.distinct()
        else:
            results = Book.objects.none()
        return render(request,'bookshop/search.html',{'search':search,'results':results})

def products(request,category_slug=None):
    """
    this function is used to show all books based on their categories

    """
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        books = books.filter(category=category)
    return render(request,'bookshop/book_list.html',{'category':category,
                                                     'categories':categories,
                                                     'books':books})

        