from rest_framework import serializers
from .models import Consultation
from dpi.serializers import DpiSerializer,MedcinListSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'medecin', 'dpi', 'etablisement', 'resume', 'la_date']

class ConsultationDetailSerializer(serializers.ModelSerializer):
    # Read-only fields for display purposes
    medecin = MedcinListSerializer(read_only=True)
    etablisement = serializers.CharField(source='etablisement.nom', read_only=True)
    dpi = DpiSerializer(read_only=True)

    class Meta:
        model = Consultation
        fields = ['id', 'medecin', 'dpi', 'etablisement', 'resume', 'la_date']

