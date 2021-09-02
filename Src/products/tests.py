from django.test import TestCase ,SimpleTestCase
from .models import Book,Category
from django.shortcuts import reverse
class BasicTest(TestCase):
    
    def setup(self):
        self.category =Category.objects.create(name ='fiction',slug = 'fiction' )
        
    def test_fields(self):
        record = Category.objects.get(pk=1)
        expected_category_name =record.name
        self.assertEquals(expected_category_name,'fiction')

   

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)

    def test_home_url_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code,200)

    # def test_correct_template(self):
    #     response = self.client.get(reverse('index'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertEquals(response,'bookshop/index.html' )

   