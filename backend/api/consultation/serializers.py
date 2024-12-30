from rest_framework import serializers
from .models import Consultation
from dpi.serializers import DpiSerializer,MedcinListSerializer
from dpi.models import Dpi,Patient

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'medecin', 'dpi', 'etablisement', 'resume', 'la_date']

class ConsultationDpiSerializer(serializers.ModelSerializer):
    # Read-only fields for display purposes
    medecin = MedcinListSerializer(read_only=True)
    etablisement = serializers.CharField(source='etablisement.nom', read_only=True)

    class Meta:
        model = Consultation
        fields = ['id', 'medecin', 'etablisement', 'resume', 'la_date']

    
class PatientSeriliazerConsultation(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'NSS', 'nom', 'prenom']

class DpiSerializerConsultation(serializers.ModelSerializer):
    id = PatientSeriliazerConsultation(read_only=True)
    class Meta:
        model = Dpi
        fields = ['id']

class ConsultationDetailSerializer(serializers.ModelSerializer):
    # Read-only fields for display purposes
    medecin = MedcinListSerializer(read_only=True)
    etablisement = serializers.CharField(source='etablisement.nom', read_only=True)
    dpi = DpiSerializerConsultation(read_only=True)

    class Meta:
        model = Consultation
        fields = ['id', 'medecin', 'dpi', 'etablisement', 'resume', 'la_date']

class ConsultationwithDpiSerializer(serializers.ModelSerializer):
    # Read-only fields for display purposes
    medecin = MedcinListSerializer(read_only=True)
    etablisement = serializers.CharField(source='etablisement.nom', read_only=True)
    class Meta:
        model = Consultation
        fields = ['id', 'medecin','dpi','etablisement', 'resume', 'la_date']




 
