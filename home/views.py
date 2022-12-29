from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product,Category
from cart.models import Cart

class HomeView(View):
    def get(self, request):
        products = Product.objects.all().order_by("-created")[:6]
        cart_products = []
        if request.user.is_authenticated:
            cart_products = Cart.Products_of_carts(Cart.objects.filter(user=request.user))
        return render(request, 'home/index.html', {"products": products,"cart_products":cart_products})


class SearchInCategoryView(View):
    def get(self,request,category_id = None):
        if category_id:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.filter().order_by("-created")
        return render(request,"home/search_page.html",{"products":products})

class SearchNavbarView(View):
    def get(self,request):
        products = Product.objects.filter(name__contains=request.GET.get("navbar_search",""))
        return render(request,"home/search_page.html",{"products":products})
# class MoreProductView(View):
#     def get(self,request,category_id,product_number):
#         pass

