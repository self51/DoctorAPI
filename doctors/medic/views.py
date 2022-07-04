from .models import Direction, Doctor
from .serializers import DirectionSerializer, DoctorSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('sort_number')
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['directions', 'experience', ]
    ordering_fields = ['birth_date', 'experience', ]
