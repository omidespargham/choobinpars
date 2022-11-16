from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, requests):
        return render(requests, 'home/home.html')
