from django.urls import path
from . import views

app_name = 'myadmin'
urlpatterns = [
    path('delete/<int:id>/', views.AdminProductDeleteView.as_view(), name='product_delete'),
    path('products/', views.AdminShowProductsView.as_view(), name='show_products'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('addproduct/<str:category>/', views.addproduct.as_view(), name='add_productt'),
]
