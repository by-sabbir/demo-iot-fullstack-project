from django.urls import path
from .views import ApiListAndCreationView
urlpatterns = [
    path('sensor-data/', ApiListAndCreationView.as_view(), name='sensor_data'),
]