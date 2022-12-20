from django.contrib import admin
from .models import Product,Category,Comment,Favorite,Repair,mobl,CategoryForm

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Repair)
admin.site.register(Favorite)
admin.site.register(mobl)
admin.site.register(CategoryForm)
