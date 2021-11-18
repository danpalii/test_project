from django.urls import path

from products.api.api_views import producs_list, snippet_detail

urlpatterns = [
    path('products/', producs_list),
    path('products/<int:pk>', snippet_detail),
]