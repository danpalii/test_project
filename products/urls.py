from django.urls import path
from products.views import new_products

app_name = 'products'

urlpatterns = [
    path('new_product/', new_products, name='new_products'),
]
