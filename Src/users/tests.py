from django.test import TestCase
from django.test import SimpleTestCase
from .forms import AddUserAddresForm

class TestAddress(SimpleTestCase):
    """
    testing the address form of user

    """
    def test_valid_data(self):
        form = AddUserAddresForm(data = {'title':'خوزستان','author':'مصطفی رحمان دوست','postal_code':'123456'})
