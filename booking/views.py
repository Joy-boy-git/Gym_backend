from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import Booking


class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by("-created_at")
    serializer_class = BookingSerializer


class BookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class DashboardApiView(APIView):
    def get(self, request):
        total_booking = Booking.objects.count()
        pending = Booking.objects.filter(status ="pending").count()
        confirmed  =Booking.objects.filter(status ="Confirmed").count()
        cancelled = Booking.objects.filter(status = "cancelled").count()
        recent = Booking.objects.order_by("-created_at")[:5]

        data ={
            "total_booking" :total_booking,
            "pending": pending,
            "confirmed" : confirmed,
            "cancelled" : cancelled,
            "recent_booking" : [
                {
                     "id": booking.id,
                    "name": booking.name,
                    "goal": booking.goal,
                    "status": booking.status,
                    "date": booking.booking_date,
                }
                for booking in recent
            ]
        }
        return Response(data)

