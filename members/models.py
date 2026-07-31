from django.db import models

# Create your models here.
class Member(models.Model):

    MEMBERSHIP_CHOICES = [
        ("Basic", "Basic"),
        ("Standard", "Standard"),
        ("Premium", "Premium"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Suspended", "Suspended"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    membership = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_CHOICES,
    )

    join_date = models.DateField()

    expiry_date = models.DateField()

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name