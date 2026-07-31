from django.db import models

class Booking(models.Model):

    FITNESS_CHOICES = [
        ("Weight Loss","Weight Loss"),
        ("Muscle Gain","Muscle Gain"),
        ("Yoga","Yoga"),
        ("Strength Training","Strength Training"),
        ("Cardio","Cardio"),
    ]

    STATUS = [
        ("Pending","Pending"),
        ("Confirmed","Confirmed"),
        ("Cancelled","Cancelled"),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    goal = models.CharField(
        max_length=50,
        choices=FITNESS_CHOICES
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





