from django.contrib import admin
from .models import Measurement


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'distance', 'created_at')



admin.site.register(Measurement, MeasurementAdmin)
