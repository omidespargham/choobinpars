from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from cart.models import Cart

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        cart_products = Cart.Products_of_carts(Cart.objects.filter(user=request.user))
        return render(request, 'home/index.html', {"products": products,"cart_products":cart_products})




