from rest_framework import serializers
from .models import Consultation
from dpi.models import Dpi, Etablisement
from authentication.models import CustomUser 

class DpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpi
        fields = '__all__'


class EtablisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablisement
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']  # Include relevant fields


class ConsultationSerializer(serializers.ModelSerializer):
    dpi = DpiSerializer()
    medecin = UserSerializer()
    etablisement = EtablisementSerializer()

    class Meta:
        model = Consultation
        fields = ['id', 'dpi', 'resume', 'la_date', 'medecin', 'etablisement']
