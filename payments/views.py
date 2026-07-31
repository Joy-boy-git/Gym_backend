from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):

    queryset = Payment.objects.select_related("member").order_by("-Payment_date")

    serializer_class = PaymentSerializer