from django.db import models
from authentication.models import CustomUser
from consultation.models import Consultation

# Create your models here.
class BilanBiologique(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    laborantient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='biological_tests',null=True,blank=True)
    satisfait = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False,default=None)

    def __str__(self):
        return f"Bilan Biologique {self.id} - {'Satisfied' if self.satisfait else 'Unsatisfied'}"


class ParamValeur(models.Model):
    id = models.AutoField(primary_key=True)
    valeur = models.FloatField()
    unite = models.CharField(max_length=255)
    parametre = models.CharField(max_length=255)
    valeur_reference = models.CharField(max_length=255)
    bilan = models.ForeignKey(BilanBiologique, on_delete=models.CASCADE)

    def __str__(self):
        return f"Param {self.parametre} - {self.valeur} {self.unite}"

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    descirption = models.CharField(max_length=255)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification {self.id} - Type: {self.type}"