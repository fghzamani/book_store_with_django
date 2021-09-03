from django import forms
from products.models import Book,Category
from users.models import Staff





class AddNewBook(forms.ModelForm):
	title = forms.CharField(label = 'عنوان',widget=forms.TextInput(attrs={'class': 'form-control'}))
	author = forms.CharField(label = 'نویسنده ',widget=forms.TextInput(attrs={'class':'form-control'}))
	publisher = forms.CharField(label = 'انتشارات ',widget=forms.TextInput(attrs={'class':'form-control'}))
	description= forms.CharField(label = 'توضیحات ',widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Book
		fields = ['title','author','price','inventory','cover','description','category','publisher','coupon']

