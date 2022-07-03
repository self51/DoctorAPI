from rest_framework import serializers

from .models import Direction, Doctor


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'name_direction', 'slug', 'sort_number',
        )


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'name', 'directions', 'description', 'birth_date', 'experience',
            'sort_number',
        )
