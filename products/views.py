from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View


from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDetailView(View):
    template = "products/product_detail.html"

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return render(request, self.template, {"product": product})
        except Product.DoesNotExist:
            return redirect("home:home")






class ProductsWithSpecificCategoryView(View):  # this is for search
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            products = None
        return render(request, "products/all_products.html", {"products": products})

# Create your views here.
