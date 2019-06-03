from django.db import models


# Create your models here.
class LNMonline(models.Model):
    Merchant_Request_ID = models.CharField(max_length=100, blank=True, null=True)
    Checkout_Request_ID = models.CharField(max_length=50, blank=True, null=True)
    Result_Code = models.IntegerField(blank=True, null=True)
    Result_Description = models.CharField(max_length=120, blank=True, null=True)
    Amount = models.FloatField(blank=True, null=True)
    Mpesa_Receipt_Number = models.CharField(max_length=15, blank=True, null=True)
    Transaction_Date = models.DateTimeField(blank=True, null=True)
    Phone_Number = models.CharField(max_length=13, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return str(self.Phone_Number)