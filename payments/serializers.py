from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    member_name = serializers.CharField(
        source="member.name",
        read_only=True,
    )

    class Meta:
        model = Payment
        fields = "__all__"