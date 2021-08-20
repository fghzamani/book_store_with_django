from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    
    title = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    price = models.BigIntegerField()
    inventory = models.IntegerField()
    cover = models.ImageField(upload_to='media/', blank=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField('Category',related_name='category')
    publisher = models.CharField(max_length=200,blank=True,null=True)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL, blank=True, null=True,related_name='coupon')
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'کتاب'
        verbose_name_plural = ' کتاب ها' 

    def __str__(self):
        return self.title

         
    def get_absolute_url(self): 
        """
        returning absolute url of each book
        
        """
        return reverse('book_detail', args=[str(self.id)])
        
    def has_inventory(self,number):
        return self.inventory>0 and self.inventory>= number
    

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
    # def checking_inventory(self):
        

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    
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
        return reverse("books:categories",kwargs={'slug':self.slug})

class Coupon(models.Model):
    COUPON_CHOISE = [('c','نقدی'),('p','درصدی')]
    coupon_type = models.CharField(max_length=1,choices=COUPON_CHOISE)
    created_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateTimeField()
    cash_amount = models.IntegerField(blank=True,null=True)
    percent_amount = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)],blank=True,null=True) 
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = " کوپن"
        verbose_name_plural = 'کوپن ها'