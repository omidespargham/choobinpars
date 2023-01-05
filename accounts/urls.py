from django.urls import path
from .views import LoginView,LoginVerifyView,UserLogoutView,UserProfileView
app_name = "accounts"

urlpatterns = [
    path('login/',LoginView.as_view(),name="user_login"),
    path('loginVerify/',LoginVerifyView.as_view(),name="user_login_verify"),
    path('logout/',UserLogoutView.as_view(),name="user_logout"),
    path('profile/',UserProfileView.as_view(),name="user_profile"),
]
