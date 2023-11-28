from django.db import models
from products.models import Product
# Create your models here.


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    # product = models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'