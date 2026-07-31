from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "goal",
        "booking_date",
        "booking_time",
        "status",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )

    list_filter = (
        "goal",
        "status",
    )