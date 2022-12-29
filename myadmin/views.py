from django.shortcuts import render, redirect
from django.views import View
from products.models import Product, Category
from myadmin.forms import AddProductForm, moblForm, check_the_form_type, ParentCategoryForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify


class AdminShowProductsView(View):
    template_name = "myadmin/admin_show_products.html"

    def get(self, request):
        products = Product.objects.all().order_by("-created")
        return render(request, self.template_name, {"products": products})


class AdminProductDeleteView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect("myadmin:show_products")


class AddProductView(LoginRequiredMixin, View):
    form_class = AddProductForm

    # dispatch dont have login required Mixin

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True and request.user.is_admin == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('home:home')
        
    # version 1 add product
    def get(self, request):
        return render(request, 'myadmin/addproduct.html', {'form': self.form_class})

    # version 1 and 2 of add product
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            categorys = cl.get("categorys")
            # category = Category.objects.filter(name__in=categorys)
            product = Product(
                user=request.user,
                # category=category,
                name=cl['name'],
                price=cl['price'],
                description=cl['description'],
            )
            # product.slug = slugify(cl['name'])
            product.save()
            product.category.set(categorys)
            messages.success(request, f"add product", "success")
            return redirect('home:home')
        return render(request, 'myadmin/addproduct.html', {'form': form})


class AddProductSelectCategoryView(LoginRequiredMixin, View):
    form_class = ParentCategoryForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True and request.user.is_admin == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('home:home')
        
    # version 2 add product (not activated)
    def get(self, request):
        return render(request,"myadmin/select_category.html",{"form":self.form_class})

    # version 2 add product (not activated)
    def post(self, request):
        form = ParentCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data["category"]
            # category = Category.objects.get(name=, parent__isnull=True)
        # except Category.DoesNotExist:
            # return redirect("home:home")
            form = check_the_form_type(category[:1])
        return render(request, 'myadmin/addproduct.html', {"form": form})


