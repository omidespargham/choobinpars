from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Category,CategoryForm



@receiver(post_save, sender=Category)
def post_save_category_form(instance, sender, created, *args, **kwargs):
    if created and instance.parent == None:
        CategoryForm.objects.create(category=instance,form_class=instance.product_related_class_name + "Form")

        