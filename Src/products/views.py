from django.shortcuts import render
from django.views.generic import ListView,FormView, DetailView,CreateView,UpdateView , DeleteView,TemplateView
from .models import Book,Category
from django.db.models import Q
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormMixin

class HomeView(TemplateView):
    model = Book
    template_name = 'bookshop/index.html' 
    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['newbook_list'] = Book.objects.all()[:4]
        # print(context)
        return context


class BookListView(ListView):
    model = Book
    template_name = 'bookshop/book_list.html'
    def get_context_data(self,**kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['cat_list'] = Category.objects.all()
        print(context)
        return context
    
    


class BookDetailView(DetailView): 
    model = Book
    template_name = 'bookshop/book_detail.html'
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm(initial={'book': self.object})
        return context
    def dispatch(self,request,*args,**kwargs):
        # print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        form = CartAddProductForm(request.POST)
        # print('FORM',form)
        if form.is_valid():
            cd = form.cleaned_data
            quantity=cd['quantity']
            print('******************************')
            print(quantity)
        return super(BookDetailView, self).dispatch(request, *args, **kwargs)
    
    
    
class BookDetailForm(FormView,FormMixin):
    template_name = 'bookshop/book_detail.html'
    form_class = CartAddProductForm
    success_url = '/cart/'


class CategoryListView(ListView):
    
    model = Category
    template_name = 'bookshop/all_category_list.html'
    

class SearchList(ListView):
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


        