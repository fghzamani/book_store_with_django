from decimal import Decimal
from django.conf import settings
from products.models import Book 
from discount.models import Discount

class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        print('cart',cart)
        if not cart:
            
            cart = self.session[settings.CART_SESSION_ID] = {} # save an empty cart in the session
        self.cart = cart
        self.discount_id = self.session.get('discount_id') # store current applied coupon
        print('SEssion',self.discount_id)
   
   
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        book_ids = self.cart.keys()
        
        # get the product objects and add them to the cart
        books = Book.objects.filter(id__in=book_ids)

        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, book, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        if book.has_inventory:
            book_id = str(book.id)
            if book_id not in self.cart:
                self.cart[book_id] = {'quantity': 0,
                                        'price': book.price}
            if override_quantity:
                self.cart[book_id]['quantity'] = quantity
            else:
                self.cart[book_id]['quantity'] += quantity
            book.removing_inventory(quantity)
            self.save()
        else:
            pass
        

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, book ):
        """
        Remove a product from the cart.
        """
        book_id = str(book.id)
        quantity = self.cart[book_id]['quantity']
      
        if book_id in self.cart:
            del self.cart[book_id]
            book.adding_inventory(quantity)
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):

        return sum([item['price'] * item['quantity'] for item in self.cart.values()])

    @property
    def discount(self):
        if self.discount_id:
            try:
                return Discount.objects.get(id=self.discount_id)
            except Discount.DoesNotExist:
                pass
        return None


    def get_total_price_after_discount(self):
          
        try:
            return self.get_total_price() - self.discount.amount * self.get_total_price()

        except:
            return  self.get_total_price()
    def get_percent(self):
        return self.discount.amount*100
    
    def get_discount(self):
        if self.discount:
            return self.discount.amount *  self.get_total_price()    
       
    
    # def checking_inventory(request_number):
    #     """
    #     request_number : the number of order item
    #     method for checking the ordered number of book with it's inventory
    #     """
    #     if Book.has_inventory and  request_number < Book.inventory:
    #         return True
