from django.db import models
<<<<<<< HEAD
from django.apps import apps
from auth.models import CustomUser
from dpi.models import Dpi

class Consultation(models.Model):
    id = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE)
    resume = models.TextField(null=True, blank=True)
    la_date = models.DateField(blank=True, null=True)
    medecin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="consultations")
    etablisement = models.ForeignKey(apps.get_model('dpi', 'Etablisement'), on_delete=models.CASCADE)
=======
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
>>>>>>> 1be9cb16177b94bdb8b12086cd7455662f14eee1

    def __str__(self):
        return f"Consultation {self.id}"
