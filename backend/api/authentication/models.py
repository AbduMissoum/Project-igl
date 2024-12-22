from django.db import models
# Create your models here.
from django.contrib.auth.models import  AbstractUser
class Etablisement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('medecin', 'Medecin'),
        ('infirmier', 'Infirmier'),
        ('laborantin', 'Laborantin'),
        ('radiologue', 'Radiologue'),
        ('admin', 'Admin'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='patient')
    etablisement = models.ForeignKey(Etablisement, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username




