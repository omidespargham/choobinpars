from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product


class HomeView(View):
    def get(self, requests):
        products = Product.objects.all()
        return render(requests, 'home/index.html', {"products": products})




