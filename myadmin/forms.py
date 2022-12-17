from django import forms
from products.models import Category

class AddProductForm(forms.Form):
    categorys = forms.ModelMultipleChoiceField(label='Category',queryset=Category.objects.all())
    name = forms.CharField()
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea())