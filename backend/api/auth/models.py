from django.db import models
from dpi.models import Etablisement
# Create your models here.

class CustomUser(models.Model):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('laboratory', 'Laboratory'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='patient')
    etablisement = models.ForeignKey(Etablisement, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username

