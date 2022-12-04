from django.urls import path
from . import views

app_name = 'myadmin'
urlpatterns = [
    path('delete/<int:id>/', views.AdminProductDeleteView.as_view(), name='product_delete'),
    path('products/', views.AdminShowProductsView.as_view(), name='show_products')
]
