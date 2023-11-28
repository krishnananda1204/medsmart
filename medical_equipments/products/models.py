from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=50)
    mfg_date = models.DateField()
    product_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    owner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'