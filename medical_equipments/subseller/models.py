from django.db import models

# Create your models here.


class Subseller(models.Model):
    subseller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subseller'