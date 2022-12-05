from django.shortcuts import render
from django.views import View
from .models import Product,Category


class ProductDetailView(View):
    template = "products/product_detail.html"

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return render(request, self.template, {"product": product})
        except Product.DoesNotExist:
            return redirect("home:home")


# class Categorys(View):
#     def get(self, request):
#         categorys = Category.objects.filter(parent__isnull=True)
#         return render(request,"products/categorys.html",{"categorys":categorys})

#     def post(self,request):
#         pass


class ProductsWithSpecificCategoryView(View): # this is for search
    def get(self,request,category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            products = None
        return render(request,"products/products.html",{"products":products})





# Create your views here.
