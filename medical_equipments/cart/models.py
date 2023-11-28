from django.db import models
from products.models import Product
from customer.models import Customer
# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=50)
    # product_id = models.IntegerField()
    product = models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE)
    quatity = models.IntegerField()
    total = models.FloatField()
    # user_id = models.IntegerField()
    user = models.ForeignKey(Customer,to_field='customer_id',on_delete=models.CASCADE)
    date = models.DateField()
    cart_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cart'