from django.test import TestCase
from django.test import SimpleTestCase
from .forms import AddNewBook

class TesstAddBookForm(SimpleTestCase):
    def test_valid_data(self):
        form = AddNewBook(data = {'title':'moon','author':'meyer','price':120000,'inventory':20,'category':'fiction'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = AddNewBook(data ={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)