from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_image', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name