from rest_framework import serializers
from .models import Measurement


class MeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
