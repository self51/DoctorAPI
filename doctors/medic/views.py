from .models import Direction, Doctor
from .serializers import DirectionSerializer, DoctorSerializer

from rest_framework import viewsets


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('-sort_number')
    serializer_class = DoctorSerializer
