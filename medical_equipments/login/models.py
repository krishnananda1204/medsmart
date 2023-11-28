from django.db import models

# Create your models here.


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_id = models.IntegerField()
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'login'