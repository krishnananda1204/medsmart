from django.db import models
from cart.models import Cart
# Create your models here.

class ProductOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField() 
    date = models.DateField()
    time = models.TimeField()
    # cart_id = models.IntegerField()
    cart = models.ForeignKey(Cart,to_field='cart_id',on_delete=models.CASCADE)
    total_amount = models.FloatField()
    order_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_order'
