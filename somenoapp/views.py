from django.db import models
from django.shortcuts import render
from .models import DeliveryReceipt

def delivery_receipt_list(request):
    # Assuming you want to fetch all DeliveryReceipt objects
    receipts = DeliveryReceipt.objects.all()
    context = {'receipts': receipts}
    return render(request, 'somemono_app/delivery_receipt_list.html', context)

    class DeliveryReceipt(models.Model):
        orderer_name = models.CharField(max_length=100)
        order_number = models.CharField(max_length=20)
        item_name = models.CharField(max_length=100)
        item_number = models.CharField(max_length=20)
        unit_price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField()
        total_amount = models.DecimalField(max_digits=10, decimal_places=2)
        payment_method = models.CharField(max_length=50)

        def __str__(self):
            return f"{self.orderer_name} - {self.order_number}"
