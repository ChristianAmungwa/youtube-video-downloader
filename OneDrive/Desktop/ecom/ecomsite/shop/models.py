from django.db import models
from django.core import validators



# Create your models here.

class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200, verbose_name='Product Name')
    name = models.CharField(max_length=200, verbose_name='Product Name')
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    file = models.FileField(upload_to='uploads', default=0)
    id = models.BigAutoField(primary_key=True)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)


    


 
    

  
   
    
