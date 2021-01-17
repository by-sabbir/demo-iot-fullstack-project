from datetime import datetime
import os

from rest_framework.fields import empty
from api.models import Measurement
from chartjs.colors import COLORS, next_color
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse


class LinerChartView(BaseLineChartView):
    
    def get_labels(self):
        query = Measurement.objects.order_by('-created_at')[:20].values()
        """Return 7 labels for the x-axis."""
        labels = [datetime.strftime(val.get('created_at'), '%H:%M')\
                  for val in query]
        return labels

    def get_providers(self):
        """Return names of datasets."""
        return ["Measurement",]

    def get_data(self):
        """Return 3 datasets to plot."""
        query = Measurement.objects.order_by('-created_at')[:20].values()
        data = [val.get('distance') for val in query\
                if val.get('distance') > 0]
        return [data]
    
    def get_colors(self):
        return next_color(COLORS[3:])


class PieChartView(LinerChartView):
    def get(self, request):
        MAX_HEIGHT = int(os.environ.get('MAX_HEIGHT'))
        left = None
        try:
            query = Measurement.objects.filter(distance__gte=1).order_by('-created_at')[0]
            left = float(query.distance)
        except:
            pass
        return JsonResponse({'data': [MAX_HEIGHT - left, left]})
