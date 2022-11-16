from django.shortcuts import render, redirect,reverse
from django.contrib.auth import logout, login, authenticate
from django.views import View
from .forms import LoginForm, LoginVerifyForm
from random import randint
from .models import RGScode, User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        request.next = request.GET.get("next")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            the_code = randint(1, 9)
            RGScode.objects.create(
                phone_number=form.cleaned_data["phone_number"], code=the_code)
            print(the_code)
            request.session["user_info"] = {
                "phone_number": form.cleaned_data["phone_number"]}
            if request.next:
                return redirect(reverse("accounts:user_login_verify") + "?next=" + request.next)
            return redirect("accounts:user_login_verify")
        return render(request, self.template_name, {"form", form})


class LoginVerifyView(View):
    form_class = LoginVerifyForm
    template_name = "accounts/login_verify.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        request.next = request.GET.get("next")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # code = form.cleaned_data["code"]
            try:
                user_info = request.session["user_info"]
                user = User.objects.get(phone_number=user_info["phone_number"])

            except User.DoesNotExist:
                rand_password = User.get_random_string()
                user = User.objects.create_user(
                    phone_number=user_info["phone_number"], password=rand_password)
                # user = authenticate(
                #     username=user.phone_number, password=rand_password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, "خوش آمدید", "success")
            if request.next:
                return redirect(request.next)
            return redirect("home:home")
        return render(request, self.template_name, {"form": form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("home:home")
# Create your views here.
