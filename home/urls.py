from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchInCategoryView.as_view(), name='all_products'),
    path('search/<int:category_id>/', views.SearchInCategoryView.as_view(), name='search_in_category'),
    path('search_navbar/', views.SearchNavbarView.as_view(), name='navbar_search'),
    # path('more_product/<int:category_id>/<int:product_number>', views.MoreProductView.as_view(), name='more_product_button'),
]
