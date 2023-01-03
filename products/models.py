from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

USER = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default="")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="child_categorys")
    product_related_class_name = models.CharField(max_length=50,null=True,blank=True)

    def get_absolute_url(self):
        return f'/search/{self.id}/'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
#  version 2 of products form 
class CategoryForm(models.Model):
    category = models.OneToOneField(Category,on_delete=models.CASCADE)
    form_class = models.CharField(max_length=50)

class Product(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    slug = models.SlugField()
    availability = models.BooleanField(default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Repair(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)


class Favorite(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  # it can be contentType
    description = models.TextField()


class mobl(Product):
    count = models.PositiveBigIntegerField()

class miz(Product):
    arz = models.PositiveIntegerField()
    tool = models.PositiveIntegerField()


    
# Create your models here.
