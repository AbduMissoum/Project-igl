from django.contrib import admin
from .models import Ordonnance, Medicament, Traitement

# Register your models here.
admin.site.register(Ordonnance)
admin.site.register(Medicament)
admin.site.register(Traitement)