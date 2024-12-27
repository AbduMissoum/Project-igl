from django.db import models
from authentication.models import CustomUser
from consultation.models import Consultation
def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)
# Create your models here.
class BilanRadiologique(models.Model):
    id = models.AutoField(primary_key=True)  
    compte_rendu = models.TextField(null=True,blank=True)  
    type = models.CharField(max_length=255) 
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)  # Foreign key to Consultation
    radiologe = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True) # Foreign key to radiologue
    satisfait = models.BooleanField(default=False)  # Boolean field with default value False
    date = models.DateField(auto_now_add=False,default=None)
    def __str__(self):
        return f"BilanRadiologique {self.id}: {self.type}"
    
class ExamenImagerieMedicale(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key
    examen_image = models.ImageField(upload_to=upload_to,null=True,blank=True)  # Path to the image, not null
    bilan = models.ForeignKey(BilanRadiologique, on_delete=models.CASCADE)  # Foreign key to BilanRadiologique

    def __str__(self):
        return f"Examen Imagerie {self.id}"
