from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('detail/<int:id>/', views.ProductDetailView.as_view(),
         name='product_detail'),
    # path("categorys/",views.Categorys.as_view(),name="category"),
    path("<slug:category_slug>/", views.ProductsWithSpecificCategoryView.as_view(), name="show_products"),
]
