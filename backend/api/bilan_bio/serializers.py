from rest_framework import serializers
from .models import ParamValeur
from rest_framework import serializers
from .models import ParamValeur,BilanBiologique

class BilanBiologiqueSerializer(serializers.ModelSerializer):
    medecin = serializers.SerializerMethodField()
    dpi_id = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = BilanBiologique
        fields = '__all__'
    def get_date(self,obj):
        return obj.consultation.la_date
    def get_medecin(self, obj):
        return obj.consultation.medecin.id  

    def get_dpi_id(self, obj):
        return obj.consultation.dpi_id.id 
class ParamValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamValeur
        fields = ['id', 'parametre', 'valeur', 'unite']

    def update(self, instance, validated_data):
        # Update the instance with new values from validated_data
        instance.valeur = validated_data.get('valeur', instance.valeur)
        instance.unite = validated_data.get('unite', instance.unite)
        instance.save()
        return instance

