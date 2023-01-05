from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from products.models import Product

class OrderView(LoginRequiredMixin,View):
    def post(self,request,product_id):
        product = Product.objects.get(id=product_id)
        order = Order.objects.create(product=product,user=request.user)
        return redirect('accounts:show_user_orders')

# Create your views here.
