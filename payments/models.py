from django.db import models
from members.models import Member
# Create your models here.

class Payment(models.Model):
    PAYMENT_METHOD = [
        ("Cash", "Cash"),
        ("Upi", "Upi"),
        ("Card", "Card"),
        ("Bank Transfer", "Bank Transfer"),
    ]

    PAYMENT_STATUS = [
        ("Paid", "Paid"),
        ("Pending", "Pending"),
        ("Failed", "Failed"),
    ]

    # example fields (add or modify as needed)
    member = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE,
        related_name="payments"
        )
    amount = models.DecimalField(
        max_digits=10,
          decimal_places=2
    )

    Payment_date = models.DateField()

    method = models.CharField(
        max_length=32,
          choices=PAYMENT_METHOD
    )
    status = models.CharField(
        max_length=16,
          choices=PAYMENT_STATUS,
          default="Paid"
    )
    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.name} - ${self.amount}"
