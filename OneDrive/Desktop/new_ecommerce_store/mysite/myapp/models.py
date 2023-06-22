from django.db import models
from django.contrib.auth.models import User
from django.core import validators
#from address.models import AddressField


# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=70, verbose_name='Product Name')

    description = models.TextField(max_length=8000,verbose_name='Description')

    home_page_description = models.TextField(max_length=20,verbose_name='Home Page Description', default='Description')

    price = models.FloatField(verbose_name='Price')

    file = models.FileField(upload_to='uploads', default=0)
    image = models.CharField(max_length=300, default=0)


    def __str__(self):
        return self.name
    




class OrderDetail(models.Model):

    id = models.BigAutoField(primary_key=True)

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(verbose_name='Customer Email')

    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.PROTECT)

    amount = models.IntegerField(verbose_name='Amount')

    stripe_payment_intent = models.CharField(max_length=200)

    # This field can be changed as status
    has_paid = models.BooleanField(default=False, verbose_name='Payment Status')

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now_add=True)

    customer_address = models.TextField(max_length=10000, default="text")



    def __str__(self):
        return str(self.product)
    
    