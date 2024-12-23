from django.db import models

from authentication.models import Etablisement,CustomUser
from dpi.models import Dpi

# Create your models here.
#juste pour les testes  
class Consultation(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key
    dpi_id = models.ForeignKey(Dpi, on_delete=models.CASCADE)  # Foreign key to Dpi
    resume = models.TextField()  # For storing textual data
    la_date = models.DateField()  # Date field
    medecin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Foreign key to Users
    etablisement = models.ForeignKey(Etablisement, on_delete=models.CASCADE)  # Foreign key to Etablisement

    def __str__(self):
        return f"Consultation {self.id}"
