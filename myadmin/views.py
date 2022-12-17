from django.shortcuts import render,redirect
from django.views import View
from products.models import Product,Category
from myadmin.forms import AddProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify



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


class AddProductView(LoginRequiredMixin,View):
    form_class = AddProductForm
    
    # dispatch dont have login required Mixin

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True and request.user.is_admin == True:
            return super().dispatch(request, *args, **kwargs)
        
        else:
            return redirect('home:home')

    def get(self, request):
        return render(request, 'products/addproduct.html', {'form': self.form_class})

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
        return render(request, 'products/addproduct.html', {'form': form})

# Create your views here.
