from django.shortcuts import redirect, render

from products.forms import ProductForm
from products.models import Product


def products(request):
    """Products main pages"""
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


def new_products(request):
    """Add new product pages"""
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.creator = request.user
            new_product.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/new_product.html', context)
