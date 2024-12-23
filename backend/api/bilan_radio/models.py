from django.db import models
from authentication.models import CustomUser
from consultation.models import Consultation
# Create your models here.
class BilanRadiologique(models.Model):
    id = models.AutoField(primary_key=True)  
    compte_rendu = models.TextField()  
    type = models.CharField(max_length=255) 
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="bilans")  # Foreign key to Consultation
    radiologe = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="radiologique_reports",null=True,blank=True) # Foreign key to radiologue
    statifait = models.BooleanField(default=False)  # Boolean field with default value False
    def __str__(self):
        return f"BilanRadiologique {self.id}: {self.type}"
    
class ExamenImagerieMedicale(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key
    examen_image_path = models.CharField(max_length=255)  # Path to the image, not null
    bilan = models.ForeignKey('BilanRadiologique', on_delete=models.CASCADE,related_name='examens')  # Foreign key to BilanRadiologique

    def __str__(self):
        return f"Examen Imagerie {self.id}"
