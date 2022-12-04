from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
USER = get_user_model()

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user =  models.ForeignKey(USER, on_delete=models.CASCADE)


    def create_unique_cart(product,user):
        try:
            Cart.objects.get(product=product,user=user)
        except Cart.DoesNotExist:
            Cart.objects.create(product=product,user=user)
    def Products_of_carts(carts):
        products = []
        for cart in carts:
            products.append(cart.product)
        return products
# Create your models here.
