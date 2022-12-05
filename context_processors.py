from products.models import Category

# return all the categorys in all templates
def categorys(request):
    categorys = Category.objects.filter(parent__isnull=True)
    return {"categorys":categorys}
