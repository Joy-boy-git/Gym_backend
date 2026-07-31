from django.urls import path
from .views import (
    BookingListCreateAPIView,
    BookingRetrieveUpdateDestroyAPIView,
)
from .views import DashboardApiView


urlpatterns = [
    path("bookings/", BookingListCreateAPIView.as_view()),
    path("bookings/<int:pk>/", BookingRetrieveUpdateDestroyAPIView.as_view()),
    path("dashboard/", DashboardApiView.as_view() ),
]