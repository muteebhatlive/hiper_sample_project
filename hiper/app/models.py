from django.db import models

# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=10, unique=True)
    bank_name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    amount = models.IntegerField()
     