from datetime import datetime
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from api.models import Measurement
from chartjs.colors import COLORS, next_color


class LineChartJSONView(BaseLineChartView):
    
    def get_labels(self):
        query = Measurement.objects.all().values()
        """Return 7 labels for the x-axis."""
        labels = [datetime.strftime(val.get('created_at'), '%H:%M')\
                  for val in query]
        return labels

    def get_providers(self):
        """Return names of datasets."""
        return ["Measurement",]

    def get_data(self):
        """Return 3 datasets to plot."""
        query = Measurement.objects.all().values()
        data = [val.get('distance') for val in query\
                if val.get('distance') > 0]
        return [data]
    
    def get_colors(self):
        return next_color(COLORS[3:])


line_chart = TemplateView.as_view(template_name='charts/index.html')
line_chart_json = LineChartJSONView.as_view()
