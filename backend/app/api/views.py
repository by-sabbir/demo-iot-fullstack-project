from rest_framework.views import APIView
from .models import Measurement
from .serializers import MeasurementModelSerializer
from rest_framework.response import Response
from rest_framework import serializers, status


class ApiListAndCreationView(APIView):

    def get(self, request):
        try:
            query = Measurement.objects.order_by('-created_at')
        except:
            query = None
        serializer = MeasurementModelSerializer(query, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = MeasurementModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status.HTTP_400_BAD_REQUEST)
