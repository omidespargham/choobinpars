from django.urls import path
from . import views

app_name = 'myadmin'
urlpatterns = [
    path('delete/<int:product_id>/', views.AdminProductDeleteView.as_view(), name='product_delete'),
    path('products/', views.AdminShowProductsView.as_view(), name='show_products'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    # version 2 add product
    # path('addproductselectcategory/', views.AddProductSelectCategoryView.as_view(), name='add_product_select_category'),

    
]


# path('addproductcategory/<str:category>/', views.AddProductWithCategoryView.as_view(), name='add_product_with_category'),