from rest_framework import serializers
from .models import BilanRadiologique,ExamenImagerieMedicale
from consultation.models import Consultation
from dpi.serializers import PatientSerializerWithNSS
from authentication.serializers import UserSerializer
from dpi.models import Patient
class ConsulationListingField(serializers.RelatedField):
    def to_representation(self, value):

        patient = value.dpi.id 
        # print (patient)  
        patient_serializer = PatientSerializerWithNSS(patient)
        # print(patient_serializer.data)
        medecin = UserSerializer(value.medecin)
        return {
            "patient": patient_serializer.data,
            "medcin": medecin.data,
        }
    class Meta:
        model = Consultation
        fields = '__all__'

class BilanRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
        fields = ['id','consultation','date']
    consultation = ConsulationListingField(many=False,read_only=True)
class BilanRadiologiqueSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
        fields = '__all__'
class ExamenImagerieMedicaleSerializer(serializers.ModelSerializer):
     class Meta:
        model = ExamenImagerieMedicale
        fields = ['id','examen_image']
        #Remember the formdata for the frontend team

class BilanRadiologiqueSerializerCompteRendu(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
        fields =  ['id','compte_rendu']
class ExamenImagerieMedicaleRetrieveSerializer(serializers.ModelSerializer):
    examen_image = serializers.ImageField(use_url=True)  # This ensures the full URL is included
    bilan = BilanRadiologiqueSerializerCompteRendu()
    class Meta:
        model = ExamenImagerieMedicale
        fields = ['id', 'bilan','examen_image']

        

