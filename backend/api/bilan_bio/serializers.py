from rest_framework import serializers
from .models import ParamValeur
from rest_framework import serializers
from .models import ParamValeur,BilanBiologique
from dpi.serializers import PatientSerializer,DpiSerializer,PatientSerializerWithNSS
from consultation.models import Consultation
from authentication.serializers import UserSerializer

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

class BilanBiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanBiologique
        fields = ['id','consultation','date']
    consultation = ConsulationListingField(many=False, read_only=True)

class ParamValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamValeur
        fields = ['id', 'parametre', 'valeur', 'unite','valeur_reference']

    def update(self, instance, validated_data):
        # Update the instance with new values from validated_data
        instance.valeur = validated_data.get('valeur', instance.valeur)
        instance.unite = validated_data.get('unite', instance.unite)
        instance.valeur_reference = validated_data.get('valeur_reference',instance.valeur_reference)
        instance.save()
        return instance

class RemplirBilanRequestSerializer(serializers.Serializer):
    param_valeurs = ParamValeurSerializer(many=True) 