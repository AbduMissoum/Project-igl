from rest_framework import serializers
from .models import Patient,Dpi
from authentication.models import CustomUser
class PatientCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
       model= Patient
       exclude  = ('id',)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
       model= Patient
       fields = '__all__'
   
    
       
    