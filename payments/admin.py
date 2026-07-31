
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "member",
        "amount",
        "method",
        "status",
        "Payment_date",
    )

    list_filter = (
        "status",
        "method",
    )

    search_fields = (
        "member__name",
        "member__email",
    )

    ordering = ("-Payment_date",)