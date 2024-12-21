from django.db import models
from authentication.models import CustomUser
class Patient(models.Model):  # Inherits from CustomUser
    id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    NSS = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    mutuelle = models.CharField(max_length=255, null=True, blank=True)
    medecin_traitant = models.ManyToManyField(CustomUser,related_name="patients") 
    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Dpi(models.Model):
    id = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"DPI for Patient: {self.id}"
