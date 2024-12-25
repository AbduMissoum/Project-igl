from rest_framework import serializers
from .models import Soins
from dpi.serializers import PatientSerializerWithNSS,UserListingField

class SoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soins
        fields = '__all__'
class SoinsSerializerDetail(serializers.ModelSerializer):
    patient  = PatientSerializerWithNSS(read_only=True)
    infirmier = UserListingField(read_only=True)
    class Meta:
        model = Soins
        fields = '__all__'

class SoinsWithPatientIdSerializer(serializers.ModelSerializer):
    infirmier = UserListingField(read_only=True)
    class Meta:
        model = Soins
        fields = '__all__'
class SoinsWithInfirmierSerializer(serializers.ModelSerializer):
    patient  = PatientSerializerWithNSS(read_only=True)

    class Meta:
        model = Soins
        fields = '__all__'