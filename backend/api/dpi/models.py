from django.db import models
from auth.models import CustomUser
# Create your models here.
class Etablisement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Patient(models.Model):  # Inherits from CustomUser
    id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    NSS = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    mutuelle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class PatientMedecin(models.Model):
    patient = models.ForeignKey(Patient, to_field='NSS', on_delete=models.CASCADE)
    medecin_traitant = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='medecins')

    def __str__(self):
        return f"Patient: {self.patient}, Medecin: {self.medecin_traitant}"


class Dpi(models.Model):
    id = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"DPI for Patient: {self.id}"
