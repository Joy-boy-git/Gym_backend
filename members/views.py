from django.shortcuts import render
from .models import Member
from .serializers import MemberSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class Memberviewset(ModelViewSet):
    queryset = Member.objects.all().order_by("created_at")

    serializer_class = MemberSerializer