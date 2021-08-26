from django.shortcuts import render
from django.views.generic import ListView,FormView, DetailView,CreateView,UpdateView , DeleteView,TemplateView
from users.models import Staff
from products.models import Book,Category
from .forms import AddNewBook
from django.urls import reverse_lazy,reverse

class BookCreateView(CreateView):
    model=Book
    template_name='profiles/add_new_book.html'
    fields = ['title','author','price','inventory','cover','description','category','publisher']
    def get_success_url(self):
        return reverse('staff_profile')

class BookUpdateView(UpdateView):
    model=Book
    fields = ['title','author','price','inventory','cover','description','category','publisher']
    template_name = 'profiles/book_edit.html'
    def get_success_url(self):
        return reverse('staff_profile')

class BookDeleteView(DeleteView):
    model=Book
    template_name = 'profiles/book_delete.html'
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class BookListView(ListView):
    model=Book
    template_name = 'profiles/book_list.html'

class NewCategoryView(CreateView):
    model=Category
    template_name = 'profiles/new_category.html'
    fields=['name','slug']
    def get_success_url(self):
        return reverse_lazy('staff_profile')

class StaffProfileView(TemplateView):
    model = Staff
    template_name='profiles/staffprofile_home.html'


