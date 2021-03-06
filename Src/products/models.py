from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator



class BestSellerManager(models.Manager):
    """
    this manger is for returning 3 books that has been sold out the most!
    """
    def best_seller_books(self):
        return self.objects.all().order_by('-number_of_sell')[:3]
class Book(models.Model):
    
    title = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    price = models.BigIntegerField()
    inventory = models.IntegerField()
    cover = models.ImageField(upload_to='media/', blank=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField('Category',related_name='book')
    publisher = models.CharField(max_length=200,blank=True,null=True)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL, blank=True, null=True,related_name='coupon')
    number_of_sell=models.IntegerField(default=0)
    objects = BestSellerManager()
    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'کتاب'
        verbose_name_plural = ' کتاب ها' 

    def __str__(self):
        return self.title

    def get_discounted_price(self):
        if self.get_coupon_type() == 'c':
            if self.price - self.coupon.get_cash_amount() <= 0 :
                return self.price
            return self.price - self.coupon.get_cash_amount()
        elif self.get_coupon_type() == 'p':
            return self.price - self.price*self.coupon.get_percent_amount()
        else:
            return self.price

    def get_absolute_url(self): 
        """
        returning absolute url of each book
        
        """
        return reverse('book_detail', args=[str(self.id)])
        
    def has_inventory(self,number):
        return self.inventory>0 and self.inventory  >= number
    

    def removing_inventory(self,number):
        """
        changing the inventory due to number of quantity of ordered book
        """
        self.inventory = self.inventory - number
        self.save()
        return self.inventory
    
    def adding_inventory(self,number):
        """
        adding to inventory if an item being removed from the cart

        """
        self.inventory = self.inventory + number
        self.save()
        return self.inventory
   
    def apply_cash_coupon(self,cash_amount):
        """
        apply the amount of cash coupon on book price

        """
        return self.price - cash_amount

    def apply_percent_coupon(self):
        """
        apply the percent coupon on price (takhfife darsadi)
        
        """
        return self.price - self.price*self.coupon.percent_amount
    
    # @property
    def get_coupon_type(self):
        if self.coupon:
            return self.coupon.coupon_type



class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    # objects = CategoryManager()
    class Meta:
        ordering = ['name']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        return absolute url of each category

        """
        return reverse("category_detail",args=[self.slug])

class Coupon(models.Model):
    COUPON_CHOISE = [('c','نقدی'),('p','درصدی')]
    coupon_type = models.CharField(max_length=1,choices=COUPON_CHOISE)
    created_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateTimeField()
    cash_amount = models.IntegerField(blank=True,null=True)
    percent_amount = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)],blank=True,null=True) 
    is_active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_date']
        verbose_name = " کوپن"
        verbose_name_plural = 'کوپن ها'

    def __str__(self):
        if self.coupon_type =='c':
            return  f'{self.cash_amount} نقدی'
        else:
            return f'{self.percent_amount} درصد'
    
    def get_cash_amount(self):
        return self.cash_amount
    
    def get_percent_amount(self):
        return self.percent_amount

    