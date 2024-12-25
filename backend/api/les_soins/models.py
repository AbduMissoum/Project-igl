from django.db import models

from authentication.models import CustomUser
from dpi.models import Patient
class Soins(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    infirmier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='soins')
    la_date = models.DateField()

    def __str__(self):
        return f"Soins {self.id} - {self.description}"
