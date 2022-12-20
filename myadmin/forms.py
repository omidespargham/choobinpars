from django import forms
from products.models import Category,mobl,miz,CategoryForm

class AddProductForm(forms.Form):
    categorys = forms.ModelMultipleChoiceField(label='Category',queryset=Category.objects.all())
    name = forms.CharField()
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea())

class moblForm(forms.ModelForm):
    class Meta:
        model = mobl
        # fields = "__all__"
        exclude = ("slug","user","availability")

class mizForm(forms.ModelForm):
    class Meta:
        model = miz
        # fields = "__all__"
        exclude = ("slug","user","availability")


def check_the_form_type(modelname):
    # if modelname == "mobl":
    #     return moblform
    # if modelname == "miz":
    #     return mizform
    # return None


    # for item in CategoryForm.objects.all():
    #     if modelname == item.category.product_related_class_name:
    #         return eval(item.form_class)
    try:
        get_form = CategoryForm.objects.get(category=modelname)
        return eval(get_form.form_class)
    except:
        pass