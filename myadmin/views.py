from django.shortcuts import render,redirect
from django.views import View
from products.models import Product


class AdminShowProductsView(View):
    template_name = "myadmin/admin_show_products.html"
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {"products": products})

class AdminProductDeleteView(View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("myadmin:show_products")


# Create your views here.
