from django.urls import path
from django.views.generic import TemplateView
from .views import LinerChartView, PieChartView


urlpatterns = [
  path('chart/', TemplateView.as_view(template_name='charts/index.html'), name='line_chart'),
  path('chartJSON/', LinerChartView.as_view(), name='line_chart_json'),
  path('pieJSON/', PieChartView.as_view(), name='pie_chart_json'),
]