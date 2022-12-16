from django.shortcuts import render,redirect
from django.views import View
from .models import Cart
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class CartAddView(LoginRequiredMixin,View):
    def get(self,request,product_id):
        product = Product.objects.get(id=product_id)
        Cart.create_unique_cart(product, request.user)
        # cart = Cart.objects.create(product=product,user=request.user)
        return redirect("cart:cart_show")

        
    def post(self,request):
        pass
class CartShowView(LoginRequiredMixin,View):
    template_name = "cart/cart_show.html"
    def get(self,request):
        carts = Cart.objects.filter(user=request.user)
        return render(request, self.template_name,{"carts":carts})
    


# add cart in chobinpars OK
# add cartshowview in urls OK i added CartAddView so
# add login register cart in navbar
# link all the system to gether 
# add login required in views that needed

