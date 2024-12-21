from django.db import models
# Create your models here.
class Etablisement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

