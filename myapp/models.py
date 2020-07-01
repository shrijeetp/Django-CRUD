from django.db import models


# Create your models here.
class CustomerRegModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repass = models.CharField(max_length=100)

    class Meta:
        db_table = "CustomerReg"
