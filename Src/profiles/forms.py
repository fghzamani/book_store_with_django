from django import forms
from products.models import Book,Category





class AddNewBook(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title','author','price','inventory','cover','description','category','publisher']
