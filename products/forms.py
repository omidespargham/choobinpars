from django import forms


class AddProductForm(forms.Form):
    category = forms.CharField(label='Category')
    name = forms.CharField()
    price = forms.IntegerField()
    slug = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
