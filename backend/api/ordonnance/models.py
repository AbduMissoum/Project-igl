from django.db import models
from consultation.models import Consultation

# Create your models here.
class Medicament(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Ordonnance(models.Model):
    id = models.AutoField(primary_key=True)
    valide = models.BooleanField(default=False)
    consultation= models.ForeignKey(Consultation, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Ordonnance {self.id} - {'Valid' if self.valide else 'Invalid'}"

class Traitement(models.Model):
    id = models.AutoField(primary_key=True)
    la_dose = models.CharField(max_length=255)
    la_durre = models.CharField(max_length=255, null=True, blank=True)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE, related_name='traitements')  # ajout du related_name

    def __str__(self):
        return f"Traitement {self.id} - Dose: {self.la_dose}"

