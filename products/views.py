from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from products.forms import AddProductForm
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


class AddProductView(View, LoginRequiredMixin):
    form_class = AddProductForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.get_username() == '':
            return redirect('home:home')
        else:
            if request.user.is_admin == True:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('home:home')

    def get(self, request):
        return render(request, 'products/addproduct.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            category = Category.objects.get(name=cl['category'])
            product = Product(
                user=request.user,
                # category=category,
                name=cl['name'],
                price=cl['price'],
                slug=cl['slug'],
                description=cl['description'],
            )
            product.save()
            product.category.add(category)
            messages.success(request, f"add product", "success")
            return redirect('home:home')
        return render(request, 'products/addproduct.html', {'form': form})


# class Categorys(View):
#     def get(self, request):
#         categorys = Category.objects.filter(parent__isnull=True)
#         return render(request,"products/categorys.html",{"categorys":categorys})

#     def post(self,request):
#         pass


class ProductsWithSpecificCategoryView(View):  # this is for search
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            products = None
        return render(request, "products/all_products.html", {"products": products})

# Create your views here.
