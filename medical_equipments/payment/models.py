from django.db import models
from product_order.models import ProductOrder
# Create your models here.


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # order_id = models.IntegerField()
    order = models.ForeignKey(ProductOrder,to_field='order_id',on_delete=models.CASCADE)
    date = models.DateField()
    payment_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'payment'
