from django.db import models
from django.apps import apps
from dpi.models import Dpi
from authentication.models import CustomUser, Etablisement

class Consultation(models.Model):
    id = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE)
    resume = models.TextField(null=True, blank=True)
    la_date = models.DateField(blank=True, null=True)
    medecin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="consultations")
    etablisement = models.ForeignKey(Etablisement, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consultation {self.id}"
