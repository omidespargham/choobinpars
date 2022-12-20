from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

# # Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="child_categorys")
#     def __str__(self) -> str:
#         return f"{self.name}"
# class product(models.Model):
#     name = models.CharField(max_length=200)
#     prise = models.PositiveIntegerField()
    
# class mobl(product):
#     count = models.PositiveIntegerField()
    
# class CategoryForm(models.Model):
#     category = models.OneToOneField(Category,on_delete=models.CASCADE)
#     name_of_model = models.CharField(max_length=100)

# class AllProducts(models.Model):
#     content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey("content_type","object_id")
#     category = models.OneToOneField(Category,on_delete=models.CASCADE,null=True,blank=True)