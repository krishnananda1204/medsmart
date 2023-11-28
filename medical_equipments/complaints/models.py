from django.db import models
from customer.models import Customer


# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)
    date = models.DateField()
    # user_id = models.IntegerField()
    user = models.ForeignKey(Customer,to_field='customer_id',on_delete=models.CASCADE)
    owner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'complaint'
