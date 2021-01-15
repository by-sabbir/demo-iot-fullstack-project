from django.db import models


class Measurement(models.Model):
    distance = models.DecimalField("Distance", max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Distance From the bin"  
