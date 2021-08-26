from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=250)
    amount = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)])
    created_date = models.DateTimeField(auto_now= True)
    expired_date = models.DateTimeField()
    active = models.BooleanField(default = True)


    class Meta:
        ordering=['-expired_date']
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیف ها'

    def __str__(self):
        return self.code
