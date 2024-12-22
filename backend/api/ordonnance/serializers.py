from rest_framework import serializers
from .models import Medicament, Ordonnance, Traitement


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'


class OrdonnanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordonnance
        fields = '__all__'


class TraitementSerializer(serializers.ModelSerializer):
    medicament = serializers.PrimaryKeyRelatedField(queryset=Medicament.objects.all())
    ordonnance = serializers.PrimaryKeyRelatedField(queryset=Ordonnance.objects.all())

    class Meta:
        model = Traitement
        fields = '__all__'

