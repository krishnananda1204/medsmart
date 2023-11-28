from django.db import models
from products.models import Product
from customer.models import Customer
# Create your models here.


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=50)
    # product_id = models.IntegerField()
    product = models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE)
    owner_id = models.IntegerField()
    date = models.DateField()
    # customer_id = models.IntegerField()
    customer = models.ForeignKey(Customer,to_field='customer_id',on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rating'