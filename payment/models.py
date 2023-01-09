from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='orders')
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='orders')



# Create your models here.
