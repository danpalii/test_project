from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Set product name'
    }))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Set product price'
    }))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'