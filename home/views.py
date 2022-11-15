from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, requests):
        return render(requests, 'home/home.html')
